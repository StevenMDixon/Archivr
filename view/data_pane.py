from view.base_component import BaseComponent
from domain.actions import Event
from tkinter import ttk, TOP, BOTH, END, HORIZONTAL

class DataPane(BaseComponent):
    def __init__(self, root, state):
        super().__init__(root, state)

    def file_data_updated(self, event):
        file = self.state.get_selected_file()
        if file:
            self.components['MediaName_Input'].delete(0, END)
            self.components['MediaName_Input'].insert(0, f"{file.file_name}")

            self.components['Year_Input'].delete(0, END)
            self.components['Year_Input'].insert(0, f"{file.year}")

            self.components['Season_Input'].delete(0, END)
            self.components['Season_Input'].insert(0, f"{file.season}")

            self.components['Networks_Input'].delete(0, END)
            self.components['Networks_Input'].insert(0, f"{file.network}")

            self.components['Runtime_Input'].delete(0, END)
            self.components['Runtime_Input'].insert(0, f"{file.runtime}")

            self.components['Resolution_Input'].delete(0, END)
            self.components['Resolution_Input'].insert(0, f"{file.resolution}")

            self.components['WaterMark_Input'].delete(0, END)
            self.components['WaterMark_Input'].insert(0, f"{file.formmated}")

            self.components['Rating_Input'].delete(0, END)
            self.components['Rating_Input'].insert(0, f"{file.rating}")
        else:
            self.components['MediaName_Input'].delete(0, END)
            self.components['Rating_Input'].delete(0, END)
            self.components['Year_Input'].delete(0, END)
            self.components['Season_Input'].delete(0, END)
            self.components['Networks_Input'].delete(0, END)
            self.components['Runtime_Input'].delete(0, END)
            self.components['Resolution_Input'].delete(0, END)
            self.components['WaterMark_Input'].delete(0, END)

    def setup(self):
        self.state.event_manager.subscribe(Event.SELECTED_FILE.value, self.file_data_updated)

        self.registerComponent('MediaName_Label', ttk.Label(self.root, text="Name: "))
        self.registerComponent('MediaName_Input', ttk.Entry(self.root))

        self.registerComponent('Year_Label', ttk.Label(self.root, text="Year: "))
        self.registerComponent('Year_Input', ttk.Entry(self.root))

        self.registerComponent('Rating_Label', ttk.Label(self.root, text="Rating: "))
        self.registerComponent('Rating_Input', ttk.Entry(self.root))
        
        self.registerComponent('Resolution_Label', ttk.Label(self.root, text="Resolution: "))
        self.registerComponent('Resolution_Input', ttk.Entry(self.root))

        self.registerComponent('Runtime_Label', ttk.Label(self.root, text="Runtime: "))
        self.registerComponent('Runtime_Input', ttk.Entry(self.root))

        self.registerComponent('Season_Label', ttk.Label(self.root, text="Season: "))
        self.registerComponent('Season_Input', ttk.Entry(self.root))

        self.registerComponent('Networks_Label', ttk.Label(self.root, text="Networks: "))
        self.registerComponent('Networks_Input', ttk.Entry(self.root))

        self.registerComponent('WaterMark_Label', ttk.Label(self.root, text="Watermark: "))
        self.registerComponent('WaterMark_Input', ttk.Entry(self.root))
        
        self.registerComponent('Separator_Horizontal', ttk.Separator(self.root, orient=HORIZONTAL))

        self.registerComponent('Format_Button', ttk.Button(self.root, text="Format Name", command=self.state.normalize_stub))

        self.registerComponent('Save_Button', ttk.Button(self.root, text="Rename and Save File"))
        self.registerComponent('Delete_Button', ttk.Button(self.root, text="Delete File"))

        self.registerComponent('Metadata_Button', ttk.Button(self.root, text="Metadata", command=self.state.get_metadata))

    def pack(self):

        self.setup()
        self.root.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        self.root.grid_columnconfigure(1, weight=1)

        self.components['MediaName_Label'].grid(row=0,column=0)
        self.components['MediaName_Input'].grid(row=0,column=1, columnspan=2, sticky="ew", padx=1, pady=5)

        self.components['Year_Label'].grid(row=1,column=0)
        self.components['Year_Input'].grid(row=1,column=1, sticky="ew", padx=1, pady=5)

        self.components['Format_Button'].grid(row=1,column=2, sticky="ew", padx=5, pady=5)

        self.components['Rating_Label'].grid(row=2,column=0)
        self.components['Rating_Input'].grid(row=2,column=1, sticky="ew", padx=1, pady=5)

        self.components['Season_Label'].grid(row=3,column=0)
        self.components['Season_Input'].grid(row=3,column=1, sticky="ew", padx=1, pady=5)

        self.components['Runtime_Label'].grid(row=4,column=0)
        self.components['Runtime_Input'].grid(row=4,column=1, sticky="ew", padx=1, pady=5)

        self.components['Metadata_Button'].grid(row=4,column=2, sticky="ew", padx=5, pady=5)

        self.components['Resolution_Label'].grid(row=5,column=0)
        self.components['Resolution_Input'].grid(row=5,column=1, sticky="ew", padx=1, pady=5)

        self.components['Networks_Label'].grid(row=6,column=0)
        self.components['Networks_Input'].grid(row=6,column=1, sticky="ew", padx=1, pady=5)

        self.components['WaterMark_Label'].grid(row=7,column=0)
        self.components['WaterMark_Input'].grid(row=7,column=1, sticky="ew", padx=1, pady=5)

        self.components['Separator_Horizontal'].grid(row=8,column=0, columnspan=2, sticky="ew", pady=10)

        

        self.components['Save_Button'].grid(row=10, column=2, sticky="ew", padx=5, pady=5)
        
        self.components['Delete_Button'].grid(row=11,column=2, sticky="ew", padx=5, pady=5)

        