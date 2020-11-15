from tkinter import *
from tkinter import messagebox
import pip

from db import *
from traveller import *
from admin import *

try:
    import mysql.connector
except:
    print('Some dependencies are not installed. Wait while they install...')
    pip.main(['install', '--user', 'mysql-connector-python'])
    import mysql.connector

def start_gui():
    global root
    root = Tk()
    root.iconbitmap("assets/bus.ico")
    root.geometry('%dx%d+0+0' % (width, height))
    root.config(bg='#f0f0f0')
    root.title('Bus Management - Home')
    root.resizable(True, True)

    Frame(root, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(root, text='Bus Management', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.41, y=10)

    Button(root, text='I am an Administrator', width=50, height=30, bg='#00ff99', command=AdminLoginWindow).place(relx=0.032, rely=0.22)
    Label(root, text='Administrator Login', font=('Arial', 20, 'bold'), bg='#f0f0f0').place(relx=0.058, rely=0.80)
    
    Button(root, text='I am an existing Traveller', width=50, height=30, bg='#00ff99', command=TravellerLoginWindow).place(relx=0.37, rely=0.22)
    Label(root, text='Traveller Login', font=('Arial', 20, 'bold'), bg='#f0f0f0').place(relx=0.42, rely=0.80)

    Button(root, text='I am a new Traveller', width=50, height=30, bg='#00ff99', command=RegisterUser).place(relx=0.7, rely=0.22)
    Label(root, text='Traveller Registration', font=('Arial', 20, 'bold'), bg='#f0f0f0').place(relx=0.725, rely=0.80)
    
    root.mainloop()

print('Connecting to DB to check the existence of tables before starting the GUI...')
Credentials()
ConnectDB()
print('Starting GUI...')
start_gui()