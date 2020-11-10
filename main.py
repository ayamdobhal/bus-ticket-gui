from tkinter import *
from db import table_check, create_tables

def start_gui():
    root = Tk()
    root.iconbitmap("assets/bus.ico")
    root.mainloop()

def close(WindowName):
    WindowName.destroy()

def exit():
    exitPrompt = messagebox.askyesno("Quit System", "Are you sure you want to quit?")
    if exitPrompt > 0:
        root.destroy()
    return 

