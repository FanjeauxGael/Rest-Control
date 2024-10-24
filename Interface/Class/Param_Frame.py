import customtkinter

from Interface.Custom_component import Custom_Component


class Param_Frame :

    def __init__(self, app) :
        self.app = app
        frame = customtkinter.CTkFrame(self.app, width=250, height=250, corner_radius=10)
        frame.pack(padx=10, pady=10, fill="both", expand=True, anchor='center')
        label_page_title = customtkinter.CTkLabel(frame, text="Parameter", font=("Helvetica", 40))
        label_page_title.place(relx=0.5, rely=0.1, anchor="center")
        username_field=Custom_Component.named_entry(frame,'Database file', '../etc/..',
                                                       ("Helvetica", 20))
        username_field.place(relx=0.5,rely=0.35,anchor="center")

