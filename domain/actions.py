from domain.state import State
import os
from dataclasses import dataclass
import re
 
@dataclass
class MediaItem():
    file_name: str
    extension: str
    path: str
    year: str = ''
    rating: str = ''
    timeslot: str = ''
    season: str = ''
    network: str = ''
    runtime: str = ''
    resolution: str = ''
    formmated: str = False

class Actions():
    video_extensions = ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v')

    def __init__(self):
        self.state = State(
           { 
               'selectedFolder': None,
               'files': [],
               'selectedFile': None
           } 
        )

    def subscribe(self, key, callback):
        if not hasattr(self, '_subscribers'):
            self._subscribers = {}
        if key not in self._subscribers:
            self._subscribers[key] = []
        self._subscribers[key].append(callback)

    def _notify_subscribers(self, key):
        if hasattr(self, '_subscribers') and key in self._subscribers:
            for callback in self._subscribers[key]:
                callback(self.state.get(key))

    def select_folder(self, folderSelectionMethod):
        folder_path_selected = folderSelectionMethod()
        self.state.set('selectedFolder', folder_path_selected)  
        self._notify_subscribers('selectedFolder')
        self.read_dir()

    def get_selected_folder(self):
        return self.state.get('selectedFolder')
    
    def get_files(self):
        return self.state.get('files')
    
    def set_files(self, files):
        self.state.set('files', files)
        self._notify_subscribers('files')

    def set_selected_file(self, index):
        self.state.set('selectedFileIndex', index)
        self._notify_subscribers('selectedFile')

    def get_selected_file(self):
        index = self.state.get('selectedFileIndex')
        files = self.get_files()
        print(files)
        if index is not None and 0 <= index < len(files):
            return files[index]
        return None
    
    def read_dir(self):
        files = []
        for dirpath, _, filenames in os.walk(self.get_selected_folder()):
            for filename in filenames:
                if filename.lower().endswith(self.video_extensions):
                    files.append(self._parseFileName(filename, dirpath))
        for file in files:
            print(file)
        self.state.set('files', files)
        self._notify_subscribers('files')

    def _parseFileName(self, file_name: str, path: str) -> MediaItem:
        name, extension = os.path.splitext(file_name)
        formatted = self._fileIncludesMeta(file_name)
        
        data = ()

        if formatted:
            data = self._parseSaneMetaData(file_name)
        else:
            data = self._parseCrazyMetaData(file_name)

        return MediaItem(
            file_name=name + extension,
            extension=extension,
            path=path,
            year= data[0],
            rating=data[1],
            timeslot=data[2],
            season=data[3],
            network=data[4],
            runtime=data[5],
            resolution=data[6],
            formmated=formatted
        )
    
    def _fileIncludesMeta(self, file_name: str) -> bool:
        pattern = re.compile(r'\[(\d{2,4}.*?)\]')
        return bool(pattern.search(file_name))
    
    def _parseCrazyMetaData(self, file_name: str):
        pattern = re.compile(r'(?<!\d)(?:19\d{2}|20\d{2})(?!\d)')
        match = pattern.search(file_name)
        year = match.group(0) if match else ''  
        return (year, '', '', '', '', '', '')

    #C:\Users\Helreizer55\Documents\GitHub\Archivr\tests
    def _parseSaneMetaData(self, file_name: str):
        # Placeholder for metadata parsing logic
        # Gerber Life Grow-Up Plan -[1994,A,A,31:12,720p,A,O]
        pattern = re.compile(r'\[(\d{2,4}.*?)\]')
        match = pattern.search(file_name)
        print(match)
        if match:
            return match.group(1).split('.')
        return ('', '', '', '', '', '', '')