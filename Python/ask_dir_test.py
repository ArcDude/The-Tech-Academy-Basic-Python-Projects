from tkinter import *
from  tkinter import filedialog, constants

window = Tk() # user input window

MyText= StringVar()

def DisplayDir(Var):
    feedback = askdirectory()
    Var.set(feedback)

Button(window, text='Browse', command=DisplayDir(MyText)).pack()
Entry(window, textvariable = MyText).pack()
Button(window, text='OK', command=window.destroy).pack()

mainloop()

