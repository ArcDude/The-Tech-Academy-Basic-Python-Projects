from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import constants, filedialog



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        self.master.title("User Info Page")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW")
        arg = self.master
        browse_button()

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)



root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Path for Directory", command=browse_button)
button2.grid(row=0, column=3)

mainloop()


