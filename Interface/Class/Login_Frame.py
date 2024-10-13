import customtkinter

from Interface.Custom_component import Custom_Component


class Login_Frame :
    def __init__(self, app) :
        frame=customtkinter.CTkFrame(app,width=500,height=500,corner_radius=10)
        frame.place(relx=0.5,rely=0.5,anchor='center')

        label_page_title= customtkinter.CTkLabel(frame, text="Login", font=("Helvetica", 40 ))
        label_page_title.place(relx=0.5,rely=0.1,anchor="center")

        username_field=Custom_Component.headed_entry(frame,'Username', 'Username',
                                                       ("Helvetica", 20))
        username_field.place(relx=0.5,rely=0.35,anchor="center")
        password_field=Custom_Component.headed_entry(frame, 'Password', 'Password...',
                                                       ("Helvetica", 20),"*")
        password_field.place(relx=0.5,rely=0.55,anchor="center")
        valid_button = customtkinter.CTkButton(frame, text="Login")
        valid_button.place(relx=0.8,rely=0.9,anchor="center")

        app.mainloop()
