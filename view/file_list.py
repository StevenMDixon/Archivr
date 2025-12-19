from view.base_component import BaseComponent
from tkinter import ttk
import tkinter as tk
from tkinter import ttk, LEFT, BOTH, Y

class FileList(BaseComponent):
    def __init__(self, root, state):
        super().__init__(root, state)

    def on_list_box_select(self, event):
        selection_indices = self.root.curselection()
        if selection_indices:
            index = selection_indices[0]
            self.state.set_selected_file(index)
        # else:
        #     self.root.selection_set(self.state.get_selected_file().index)
        
    def populate(self):
        self.root.delete(0, tk.END)
        items = self.state.get_files()
        for item in items:
            self.root.insert(tk.END, item.file_name + item.extension)

    def setup(self):
        self.state.subscribe('files', lambda files: self.populate())
        self.root.bind('<<ListboxSelect>>', self.on_list_box_select)

    def pack(self):
        self.setup()
        self.root.grid(row=1, column=0, columnspan=2, sticky="ewns")

        for childComponent in self.components:
             self.components[childComponent].pack()