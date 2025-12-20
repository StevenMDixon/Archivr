from tkinter import ttk, LEFT, BOTH, Y
from tkinter import filedialog, Listbox, SINGLE
from view.base_component import BaseComponent
from view.file_list import FileList
from domain.actions import Event

class LeftPanel(BaseComponent):
    def __init__(self, root, state):
        super().__init__(root, state)

    def _open_file_dialog(self):
            folder_path = filedialog.askdirectory(
                initialdir="./", 
                title="Select a folder"
                )
            return folder_path

    def setup(self):

        self.registerComponent('select_folder_button', BaseComponent(ttk.Button(self.root, text="Select Folder", command=lambda: self.state.select_folder(self._open_file_dialog)), state=self.state))
        self.registerComponent('selected_folder_label', BaseComponent(ttk.Label(self.root, text="No folder selected"), state=self.state))
        self.registerComponent('file_list', FileList(Listbox(self.root, selectmode=SINGLE, height=6), state=self.state))

        self.state.event_manager.subscribe(Event.SELECTED_FOLDER.value, lambda folder: self.components['selected_folder_label'].root.config(text=folder[-50:] or "No folder selected"))

    def pack(self):
        self.setup()
        self.root.pack(side=LEFT, expand=True, fill=BOTH)

        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.components['select_folder_button'].root.grid(row=0,column=0)
        self.components['selected_folder_label'].root.grid(row=0,column=1)
        self.components['file_list'].pack()

        # for childComponent in self.components:
        #      self.components[childComponent].pack()