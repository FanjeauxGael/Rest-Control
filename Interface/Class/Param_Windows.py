from tkinter import messagebox

import customtkinter

from Interface.Class.CTkWindows import CTkWindows
from Interface.Class.Param_Frame import Param_Frame
from Interface.Custom_component.Custom_Component import windows_enable


class Param_Windows(CTkWindows):

    def __init__(self, size, title, main_window):
        super().__init__(size, title)
        self.main_window=main_window
        Param_Frame(self.app)
        self.app.protocol("WM_DELETE_WINDOW", self.on_close)


    def on_close(self):
        response = messagebox.askokcancel("Quit", "The data has changed. Do you want to quit?")
        if response:
            windows_enable(self.main_window)
            self.app.destroy()
