from view.base_component import BaseComponent
from tkinter import ttk, RIGHT, BOTH, END

class RightPanel(BaseComponent):

    def __init__(self, root, state):
        super().__init__(root, state)

    def file_data_updated(self, event):
        file = self.state.get_selected_file()
        print(f"Selected File Updated: {file}")
        if file:
            self.components['MediaName_Input'].root.delete(0, END)
            self.components['MediaName_Input'].root.insert(0, f"{file.file_name}")

            self.components['Year_Input'].root.delete(0, END)
            self.components['Year_Input'].root.insert(0, f"{file.year}")

            self.components['TimeSlot_Input'].root.delete(0, END)
            self.components['TimeSlot_Input'].root.insert(0, f"{file.timeslot}")

            self.components['Season_Input'].root.delete(0, END)
            self.components['Season_Input'].root.insert(0, f"{file.season}")

            self.components['Networks_Input'].root.delete(0, END)
            self.components['Networks_Input'].root.insert(0, f"{file.network}")

            self.components['Runtime_Input'].root.delete(0, END)
            self.components['Runtime_Input'].root.insert(0, f"{file.runtime}")

            self.components['Resolution_Input'].root.delete(0, END)
            self.components['Resolution_Input'].root.insert(0, f"{file.resolution}")

            self.components['WaterMark_Input'].root.delete(0, END)
            self.components['WaterMark_Input'].root.insert(0, f"{file.formmated}")
        else:
            self.components['MediaName_Input'].root.delete(0, END)
            self.components['Year_Input'].root.delete(0, END)
            self.components['TimeSlot_Input'].root.delete(0, END)
            self.components['Season_Input'].root.delete(0, END)
            self.components['Networks_Input'].root.delete(0, END)
            self.components['Runtime_Input'].root.delete(0, END)
            self.components['Resolution_Input'].root.delete(0, END)
            self.components['WaterMark_Input'].root.delete(0, END)

    def setup(self):
        self.state.subscribe('selectedFile', self.file_data_updated)

        self.registerComponent('Message', BaseComponent(ttk.Label(self.root, text="Lets Fix Your Files!"), state=self.state))

        self.registerComponent('MediaName_Label', BaseComponent(ttk.Label(self.root, text="Media Name: "), state=self.state))
        self.registerComponent('MediaName_Input', BaseComponent(ttk.Entry(self.root), state=self.state))

        self.registerComponent('Year_Label', BaseComponent(ttk.Label(self.root, text="Year: "), state=self.state))
        self.registerComponent('Year_Input', BaseComponent(ttk.Entry(self.root), state=self.state))

        self.registerComponent('TimeSlot_Label', BaseComponent(ttk.Label(self.root, text="Time Slot: "), state=self.state))
        self.registerComponent('TimeSlot_Input', BaseComponent(ttk.Entry(self.root), state=self.state))

        self.registerComponent('Season_Label', BaseComponent(ttk.Label(self.root, text="Season: "), state=self.state))
        self.registerComponent('Season_Input', BaseComponent(ttk.Entry(self.root), state=self.state))

        self.registerComponent('Networks_Label', BaseComponent(ttk.Label(self.root, text="Networks: "), state=self.state))
        self.registerComponent('Networks_Input', BaseComponent(ttk.Entry(self.root), state=self.state))

        self.registerComponent('Runtime_Label', BaseComponent(ttk.Label(self.root, text="Runtime: "), state=self.state))
        self.registerComponent('Runtime_Input', BaseComponent(ttk.Entry(self.root), state=self.state))

        self.registerComponent('Resolution_Label', BaseComponent(ttk.Label(self.root, text="Resolution: "), state=self.state))
        self.registerComponent('Resolution_Input', BaseComponent(ttk.Entry(self.root), state=self.state))

        self.registerComponent('WaterMark_Label', BaseComponent(ttk.Label(self.root, text="Watermark: "), state=self.state))
        self.registerComponent('WaterMark_Input', BaseComponent(ttk.Entry(self.root), state=self.state))


    def pack(self):
        self.setup()
        self.root.pack(side=RIGHT, expand=True)

        # self.components['Message'].root.pack()
        self.components['MediaName_Label'].root.grid(row=0,column=0)
        self.components['MediaName_Input'].root.grid(row=0,column=1)
        self.components['Year_Label'].root.grid(row=1,column=0)
        self.components['Year_Input'].root.grid(row=1,column=1)
        self.components['TimeSlot_Label'].root.grid(row=2,column=0)
        self.components['TimeSlot_Input'].root.grid(row=2,column=1)
        self.components['Season_Label'].root.grid(row=3,column=0)
        self.components['Season_Input'].root.grid(row=3,column=1)
        self.components['Networks_Label'].root.grid(row=4,column=0)
        self.components['Networks_Input'].root.grid(row=4,column=1)
        self.components['Runtime_Label'].root.grid(row=5,column=0)
        self.components['Runtime_Input'].root.grid(row=5,column=1)
        self.components['WaterMark_Label'].root.grid(row=6,column=0)
        self.components['WaterMark_Input'].root.grid(row=6,column=1)
        self.components['Resolution_Label'].root.grid(row=7,column=0)
        self.components['Resolution_Input'].root.grid(row=7,column=1)