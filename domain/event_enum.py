from enum import Enum

class Event(Enum):
    SELECTED_FOLDER = 'selectedFolder'
    FILES = 'files'
    SELECTED_FILE = 'selectedFile'