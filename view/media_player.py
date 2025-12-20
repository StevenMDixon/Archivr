from view.base_component import BaseComponent
import tkinter as tk
import vlc
import sys
from domain.actions import Event
from tkinter import BOTTOM
import os

class MediaPlayer(BaseComponent):
    def __init__(self, root, state):
        super().__init__(root, state)

    def _on_selected_file(self, event):
        file = self.state.get_selected_file()
        if file:
            fileLocation = os.path.join(file.path, file.file_name + file.extension)
            media = self.instance.media_new(fileLocation)
            self.player.set_media(media)
            self.player.play()
        else: 
            self.player.stop()

    def _on_selected_folder(self, event):
        folder = self.state.get_selected_folder()
        if folder:
            self.player.stop()
            
    def setup(self):
        self.state.event_manager.subscribe(Event.SELECTED_FILE.value, self._on_selected_file)
        self.state.event_manager.subscribe(Event.SELECTED_FOLDER.value, self._on_selected_folder)

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.registerComponent('VideoFrame', tk.Frame(self.root, bg="black"))
        

    def pack(self):
        self.setup()
        self.root.pack(side=BOTTOM, fill=tk.BOTH, expand=1)

        self.components['VideoFrame'].pack(fill=tk.BOTH, expand=1)
        self.player.set_hwnd(self.components['VideoFrame'].winfo_id())