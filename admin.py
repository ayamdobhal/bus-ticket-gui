from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

from db import *

def AdminLogin():
    password = AdminPassword.get()
    print('Password: ', '*' * len(password))
    if password == 'admin':
        AdminLoginPage.destroy()
        print('Logged in successfully...')
        AdminHome()
    else:
        AdminLoginPage.destroy()
        print('Login Failed...')
        messagebox.showinfo('Error!', 'Incorrect password...')

def AdminLoginWindow():
    global AdminLoginPage
    global AdminPassword
    AdminLoginPage = Tk()
    AdminLoginPage.iconbitmap('assets/bus.ico')
    AdminLoginPage.geometry('%dx%d+0+0' % (width, height))
    AdminLoginPage.title('Admin Login')
    AdminLoginPage.resizable(True, True)
    AdminLoginPage.config(bg='#f0f0f0')

    Frame(AdminLoginPage, height=70, width=width, bg='#00ff99').place(x=0, y=0)
    Label(AdminLoginPage, font=('impact', 30, 'bold'), text = 'Admin Login', bg='#00ff99').place(relx=0.43, y=10)

    Label(AdminLoginPage, text='Admin', bg='#f0f0f0', font=('Arial', 20, 'bold')).place(relx=0.48, rely=0.36)
    Label(AdminLoginPage, text='Password', bg='#f0f0f0', font=('Arial', 20)).place(relx=0.35, rely=0.45)
    
    AdminPassword = ttk.Entry(AdminLoginPage, font=('Arial', 20), show='*')
    AdminPassword.place(relx=0.45, rely=0.45)
    Button(AdminLoginPage, text ='LOGIN', font=('Arial', 20, 'bold'), bg='#00ff99', fg='#f0f0f0', command=AdminLogin).place(relx=0.46, rely=0.55)

def AddBus():
    global AddBusForm
    AddBusForm = Tk()
    AddBusForm.iconbitmap('assets/bus.ico')
    AddBusForm.geometry('%dx%d+0+0' % (width, height))
    AddBusForm.resizable(True, True)
    AddBusForm.title('Edit Bus Database')
    AddBusForm.config(bg='#f0f0f0')
    Frame(AddBusForm, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(AddBusForm, text='Editing Bus Database', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.42, y=10)
    AddBusForm.Left = ttk.Frame(AddBusForm, width=width/2, height=1000, relief='raise')
    AddBusForm.Left.place(x=2, y=70)
    Label(AddBusForm, text='Add a New Bus', font=('Arial Black', 10, 'bold'), bg='#f0f0f0').place(x=210, y=88)

    global bus_id
    global bus_name

    Label(AddBusForm, text='Bus ID', font=('Helvetica', 8, 'bold'), bg='#f0f0f0').place(x=150, y=135)
    Label(AddBusForm, text='Bus Name', font=('Helvetica', 8, 'bold'), bg='#f0f0f0').place(x=150, y=170)

    bus_id = ttk.Entry(AddBusForm, width=15)
    bus_id.place(x=220, y=135)
    bus_name = ttk.Entry(AddBusForm, width=15)
    bus_name.place(x=220, y=170)

    ttk.Button(AddBusForm, text='ADD', command=WriteBuses, width=20).place(x=180, y=215)
    ttk.Button(AddBusForm, text='REFRESH', command=ReadBuses, width=20).place(x=180, y=260)
    ttk.Button(AddBusForm, text='EXIT', command=ExitAddBuses, width=20).place(x=180, y=305)

    AddBusForm.Right = ttk.Frame(AddBusForm, width=width/2, height=500, relief='raise')
    AddBusForm.Right.place(relx=0.6, y=70)

    global BusList

    scrollbarx = Scrollbar(AddBusForm.Right, orient=VERTICAL)
    scrollbary = Scrollbar(AddBusForm.Right, orient=HORIZONTAL)
    BusList = ttk.Treeview(AddBusForm.Right, columns=("bus_id", "bus_name"), selectmode='extended', height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=BusList.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=BusList.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    BusList.heading('bus_id', text='ID', anchor=W)
    BusList.heading('bus_name', text='Bus Name', anchor=W)

    BusList.column('#0', stretch=NO, minwidth=0, width=0)
    BusList.column('#1', stretch=NO, minwidth=0, width=120)
    
    BusList.pack()
    ReadBuses()

def ReadBuses():
    BusList.delete(*BusList.get_children())
    connection, cursor = ConnectDB()
    cursor.execute('''select * from buses order by 'bus_id';''')
    fetch = cursor.fetchall()
    for data in fetch:
        BusList.insert('', 'end', values=(data[0], data[1]))
    connection.close()
    print('Bus list refreshed...')

def WriteBuses():
    if bus_id.get() == '' or bus_name.get() == '':
        messagebox.showinfo('Requirement!', 'Please enter all the values...')
    else:
        connection, cursor = ConnectDB()
        cursor.execute('''insert into buses values({}, '{}');'''.format(bus_id.get(), bus_name.get()))
        connection.commit()
        connection.close()
        print('Added the bus to the DB...')

def ExitAddBuses():
    AddBusForm.destroy()

def RemoveBus():
    global RemoveBusForm
    RemoveBusForm = Tk()
    RemoveBusForm.geometry('%dx%d+0+0' % (width, height))
    RemoveBusForm.resizable(True, True)
    RemoveBusForm.title('Editing Bus Database')
    RemoveBusForm.config(bg='#f0f0f0')
    Frame(RemoveBusForm, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(RemoveBusForm, text='Editing Bus Database', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.42, y=10)
    RemoveBusForm.Left = ttk.Frame(RemoveBusForm, width=width/2, height=1000, relief='raise')
    RemoveBusForm.Left.place(x=2, y=70)
    Label(RemoveBusForm, text='Remove a Bus from Database', font=('Arial Black', 10, 'bold'), bg='#f0f0f0').place(x=210, y=88)

    global bus_id

    Label(RemoveBusForm, text='Bus ID', font=('Helvetica', 8, 'bold'), bg='#f0f0f0').place(x=150, y=135)
    
    bus_id = ttk.Entry(RemoveBusForm, width=15)
    bus_id.place(x=220, y=135)

    ttk.Button(RemoveBusForm, text='REMOVE', command=DelBus, width=20).place(x=180, y=215)
    ttk.Button(RemoveBusForm, text='REFRESH', command=ReadBuses, width=20).place(x=180, y=260)
    ttk.Button(RemoveBusForm, text='EXIT', command=ExitRmBuses, width=20).place(x=180, y=305)

    RemoveBusForm.Right = ttk.Frame(RemoveBusForm, width=width/2, height=500, relief='raise')
    RemoveBusForm.Right.place(relx=0.6, y=70)

    global BusList

    scrollbarx = Scrollbar(RemoveBusForm.Right, orient=VERTICAL)
    scrollbary = Scrollbar(RemoveBusForm.Right, orient=HORIZONTAL)
    BusList = ttk.Treeview(RemoveBusForm.Right, columns=("bus_id", "bus_name"), selectmode='extended', height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=BusList.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=BusList.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    BusList.heading('bus_id', text='ID', anchor=W)
    BusList.heading('bus_name', text='Bus Name', anchor=W)

    BusList.column('#0', stretch=NO, minwidth=0, width=0)
    BusList.column('#1', stretch=NO, minwidth=0, width=120)
    
    BusList.pack()
    ReadBuses()

def DelBus():
    if bus_id.get() == '':
        messagebox.showinfo('Required!', 'Enter all values...')
    connection, cursor = ConnectDB()
    cursor.execute('''delete from buses where bus_id='{}';'''.format(bus_id.get()))
    connection.commit()
    connection.close()
    print('Removed bus from the DB...')

def ExitRmBuses():
    RemoveBusForm.destroy()

def AdminHome():
    global AdminHomePage
    AdminHomePage = Tk()
    AdminHomePage.iconbitmap('assets/bus.ico')
    AdminHomePage.geometry('%dx%d+0+0' % (width, height))
    AdminHomePage.resizable(True, True)
    AdminHomePage.title('Admin Dashboard')
    AdminHomePage.config(bg='#f0f0f0')
    Frame(AdminHomePage, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(AdminHomePage, text='Admin Dashboard', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.4, y=10)
    Button(AdminHomePage, text='Add a Bus to Database', font=('Arial Black', 10), width=50, height=30, bg='#00ff99', fg='#f0f0f0', bd=6, command=AddBus).place(relx=0.1, rely=0.2)
    Button(AdminHomePage, text='Remove a Bus from Database', font=('Arial Black', 10), width=50, height=30, bg='#00ff99', fg='#f0f0f0', bd=6, command=RemoveBus).place(relx=0.6, rely=0.2)
