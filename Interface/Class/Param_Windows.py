import customtkinter

from Interface.Class.CTkWindows import CTkWindows


class Param_Windows(CTkWindows):

    def __init__(self, size, title):
        super().__init__(size, title)
        frame = customtkinter.CTkFrame(self.app, width=500, height=500, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor='center')
