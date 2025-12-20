import os
import re
import ffmpeg

from domain.date_normalizer import DateNormalizer
from domain.media_item import MediaItem
from domain.state import State
from domain.event_enum import Event
from domain.event_manager import EventManager

class Actions():
    video_extensions = ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v')

    def __init__(self):
        self.state = State(
           { 
               'selectedFolder': None,
               'files': [],
               'selectedFileIndex': -1
           } 
        )
        self.event_manager = EventManager()

    def select_folder(self, folderSelectionMethod):
        folder_path_selected = folderSelectionMethod()
        self.state.set('selectedFolder', folder_path_selected)  
        self.event_manager._notify_subscribers(Event.SELECTED_FOLDER.value)

        if (self.state.get('selectedFileIndex') > 0):
            self.set_selected_file(-1)

        self._read_dir()

    def get_selected_folder(self):
        return self.state.get('selectedFolder')
    
    def get_files(self):
        return self.state.get('files')
    
    def set_files(self, files):
        self.state.set('files', files)
        self.event_manager._notify_subscribers(Event.FILES.value)

    def set_selected_file(self, index):
        self.state.set('selectedFileIndex', index)
        self.event_manager._notify_subscribers(Event.SELECTED_FILE.value)
    
    def get_selected_file(self):
        index = self.state.get('selectedFileIndex')
        files = self.get_files()

        if index is not None and 0 <= index < len(files):
            return files[index]
        return None
    
    def _read_dir(self):
        files = []
        index = 0
        for dirpath, _, filenames in os.walk(self.get_selected_folder()):
            for filename in filenames:
                if filename.lower().endswith(self.video_extensions):
                    files.append(self._parseFileName(filename, dirpath, index))
                    index += 1
        
        files.sort(key=lambda x: x.file_name)
        self.state.set('files', files)
        self.event_manager._notify_subscribers(Event.FILES.value)

    def _parseFileName(self, file_name: str, path: str, index: int) -> MediaItem:
        name, extension = os.path.splitext(file_name)
        formatted = self._fileIncludesMeta(file_name)
        
        data = ()

        if formatted:
            data = self._parseSaneMetaData(file_name)
        else:
            data = self._parseCrazyMetaData(file_name)

        return MediaItem(
            file_name=name,
            normalized_name=name,
            extension=extension,
            path=path,
            year= data[0],
            rating=data[1],
            season=data[2],
            runtime=data[3],
            resolution=data[4],
            network=data[5],
            watermark=data[6],  
            formmated=formatted,
            index=index
        )
    
    def _fileIncludesMeta(self, file_name: str) -> bool:
        pattern = re.compile(r'\[(\d{2,4}.*?)\]')
        return bool(pattern.search(file_name))
    
    def _parseCrazyMetaData(self, file_name: str):
        pattern = re.compile(r'(?<!\d)(?:19\d{2}|20\d{2})(?!\d)')
        match = pattern.search(file_name)
        year = match.group(0) if match else ''  
        return (year, '', '', '', '', '', '')

    def _parseSaneMetaData(self, file_name: str):
        pattern = re.compile(r'\[(\d{2,4}.*?)\]')
        match = pattern.search(file_name)
        print(match)
        if match:
            return match.group(1).split('.')
        return ('', '', '', '', '', '', '')
    
    def normalize_stub(self):
        file = self.get_selected_file()
        if file:
            file.file_name = DateNormalizer.normalize(file.file_name)
            self.event_manager._notify_subscribers(Event.SELECTED_FILE.value)

    def get_metadata(self):
        file = self.get_selected_file()
        if not file:
            return
        filepath = os.path.join(file.path, file.file_name + file.extension)
        try:
            probe = ffmpeg.probe(filepath)
            format_info = probe.get('format', {})
            duration = float(format_info.get('duration', 0))

            video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
            if video_stream:
                width = int(video_stream.get('width', 0))
                height = int(video_stream.get('height', 0))
                file.resolution = f"{width}x{height}"
            
            file.runtime = duration
            self.event_manager._notify_subscribers(Event.SELECTED_FILE.value)
            
        except ffmpeg.Error as e:
            print(f"FFmpeg error: {e.stderr.decode('utf8')}")
        except Exception as e:
            print(f"An error occurred: {e}")
