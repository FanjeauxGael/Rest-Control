import os
from tkinter import PhotoImage

import customtkinter

from Interface.Class.CTkWindows import CTkWindows
from Interface.Class.Param_Windows import Param_Windows
from Interface.Custom_component.Custom_Component import image_frame, windows_disable


class DefaultWindows(CTkWindows) :

    def __init__(self, size, title):
        super().__init__(size, title)
        self.app.iconphoto(True, PhotoImage(file='Resources/images/logo.png'))
        image_path = os.path.join(os.path.dirname(__file__), '../../Resources/images/')
        img_frame = image_frame(self.app, image_path + 'parameter.png', image_path + 'parameterW.png', '')
        img_frame.event_add('<<open-param-windows>>','<Button-1>')
        img_frame.bind('<<open-param-windows>>', self.open_param)
        img_frame.place(relx=0.02, rely=0.03, anchor="center")

    def open_param(self,event):
        windows_disable(self.app)
        Param_Windows(size='600x400', title="Parameter", main_window=self.app)

