import customtkinter

from PIL import Image


def headed_entry(master, header, placeholder, font, show=""):
    frame=customtkinter.CTkFrame(master,fg_color="transparent", border_width=0)
    customtkinter.CTkLabel(frame, text=header, font=font).pack()

    customtkinter.CTkEntry(frame, placeholder_text=placeholder, show=show).pack()
    return frame

def image_frame(master, l_image='', d_image='', cursor=''):
    def_image= customtkinter.CTkImage(light_image=Image.open(l_image),
                                       dark_image=Image.open(d_image),size=(40,40))
    return customtkinter.CTkLabel(master,text="", image=def_image, cursor=cursor)

def windows_disable(windows):
    for child in windows.winfo_children():
        if check_frame(child) is False:
            child.configure(state='disabled')


def check_frame(child):
    if child.widgetName == 'frame':
        for frame_child in child.winfo_children():
            if check_frame(frame_child) is False:
                child.configure(state='disabled')
            else:
                check_frame(frame_child)
        return True
    return False