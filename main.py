from Interface.Class.DefaultWindows import DefaultWindows
from Interface.Class.Login_Frame import Login_Frame

if __name__ == '__main__':
    frame = DefaultWindows('1200x750',"Rest'Control")

    Login_Frame(frame.app)


