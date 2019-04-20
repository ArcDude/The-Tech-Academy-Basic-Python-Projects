from tkinter import *
import tkinter as tk
from os import *
import shutil 
import sqlite3

import pythonDbDrill
import pythonDrill_1


conn = sqlite3.connect('move.db')


shutil.move('academy.db', 'move.db')

conn = sqlite3.connect('move.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_file2, col_file5 FROM tbl_fileList")
    conn.commit()
    varText = cur.fetchall()
    for text in varText:
        msg = "File Name1: {}\nFile Name2: {}".format(text[0], text[1])
    print(msg)
conn.close()
