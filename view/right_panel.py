from view.base_component import BaseComponent
from tkinter import ttk, RIGHT, BOTH, END, RAISED
from view.data_pane import DataPane
from view.media_player import MediaPlayer

class RightPanel(BaseComponent):

    def __init__(self, root, state):
        super().__init__(root, state)

    def setup(self):
        self.registerComponent('DataPane', DataPane(ttk.Frame(self.root), state=self.state))
        self.registerComponent('MediaPlayer', MediaPlayer(ttk.Frame(self.root), state=self.state))

    def pack(self):
        self.setup()
        self.root.pack(side=RIGHT, expand=True, fill=BOTH)

        self.components['DataPane'].pack()
        self.components['MediaPlayer'].pack()