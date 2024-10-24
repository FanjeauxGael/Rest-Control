import customtkinter

from PIL import Image


def headed_entry(master, header, placeholder, font, show=""):
    frame=customtkinter.CTkFrame(master,fg_color="transparent", border_width=0)
    customtkinter.CTkLabel(frame, text=header, font=font).pack()

    customtkinter.CTkEntry(frame, placeholder_text=placeholder, show=show).pack()
    return frame

def named_entry(master, header, placeholder, font, show="", side="left"):
    frame=customtkinter.CTkFrame(master,fg_color="transparent", border_width=0)
    customtkinter.CTkLabel(frame, text=header, font=font).pack(side=side)

    customtkinter.CTkEntry(frame, placeholder_text=placeholder, show=show).pack(padx=5,side=side)
    return frame

def image_frame(master, l_image='', d_image='', cursor=''):
    def_image= customtkinter.CTkImage(light_image=Image.open(l_image),
                                       dark_image=Image.open(d_image),size=(40,40))
    return customtkinter.CTkLabel(master,text="", image=def_image, cursor=cursor)

def windows_disable(windows):
    for child in windows.winfo_children():
        if check_frame(child, 'disabled') is False:
            child.configure(state='disabled')

def windows_enable(windows):
    for child in windows.winfo_children():
        if check_frame(child, 'normal') is False:
            child.configure(state='normal')

def check_frame(child , state_value):
    if child.widgetName == 'frame':
        for frame_child in child.winfo_children():
            if check_frame(frame_child, state_value) is False:
                child.configure(state=state_value)
            else:
                check_frame(frame_child, state_value)
        return True
    return False