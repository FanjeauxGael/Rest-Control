import os
from tkinter import PhotoImage

import customtkinter

from Interface.Custom_component.Custom_Component import image_frame


class CTkWindows :
    def __init__(self, size, title):
        self.app = customtkinter.CTk()
        self.app.title(title)
        self.app.geometry(size)


