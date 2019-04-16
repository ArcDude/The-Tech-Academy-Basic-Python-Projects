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
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master
        load_gui(self)

def load_gui(self):
    self.lbl_uname = tk.Label(self.master,text = 'User Name:')
    self.lbl_uname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_status = tk.Label(self.master,text='Status:')
    self.lbl_status.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    

    self.txt_uname = tk.Entry(self.master,text='')
    self.txt_uname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_status = tk.Entry(self.master,text='')
    self.txt_status.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)


    self.btn_close = tk.Button(self.master,width=12,height=2,text='OK',command=lambda: ask_quit(self))
    self.btn_close.grid(row=3,column=0,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

def ask_quit(self):
    if tk.messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()

    root.directory = filedialog.askdirectory()
    print (root.directory)
        
if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
