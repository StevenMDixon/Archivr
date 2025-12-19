import tkinter
from tkinter import ttk
import tkinter as tk
import sv_ttk

from view.left_panel import LeftPanel
from view.right_panel import RightPanel

class GuiBase():

    def __init__(self, state):
        self.state = state
        self.root = tkinter.Tk()
        self.root.geometry("1000x800")
        sv_ttk.use_dark_theme()
        self.components = {}

        self._setup()
    
    def _setup(self):
        self.components['left_panel'] = LeftPanel(tk.Frame(self.root, width=700, height=800, bd=3, relief= tk.SUNKEN), state=self.state)
        self.components['right_panel'] = RightPanel(tk.Frame(self.root, width=300, height=800), state=self.state)

        for name, childComponent in self.components.items():
            print(f"Adding child component: {name} -> {childComponent}")
            childComponent.pack()

    def run(self):
        self.root.mainloop()




