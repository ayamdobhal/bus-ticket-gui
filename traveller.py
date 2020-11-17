from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import random

from db import *

def TravellerLogin():
    global username
    username = TravellerUsername.get()
    password = TravellerPassword.get()

    print('Username: ', username)
    print('Password: ', '*' * len(password))
    
    connection, cursor = ConnectDB()
    
    cursor.execute('''select username from customer where username='{}';'''.format(username))
    if cursor.fetchone() == None:
        TravellerLoginPage.destroy()
        messagebox.showinfo('Error!', 'Username does not exist...')
        print('Login failed!')

    cursor.execute('''select password from customer where username='{}';'''.format(username))
    if cursor.fetchone()[0] != password:
        TravellerLoginPage.destroy()
        messagebox.showinfo('AuthError', 'Incorrect password for {}.'.format(username))
        print('Login failed(incorrect password).')
    connection.close()
    TravellerLoginPage.destroy()
    print('Login successful.')
    TravellerHome(username)

def TravellerLoginWindow():
    global TravellerLoginPage
    global TravellerUsername
    global TravellerPassword
    TravellerLoginPage = Tk()
    TravellerLoginPage.iconbitmap('assets/bus.ico')
    TravellerLoginPage.geometry('%dx%d+0+0' % (width, height))
    TravellerLoginPage.title('Traveller Login')
    TravellerLoginPage.resizable(True, True)
    TravellerLoginPage.config(bg='#f0f0f0')

    Frame(TravellerLoginPage, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(TravellerLoginPage, font=('impact', 30, 'bold'), text = 'Traveller Login', bg='#00ff99').place(relx=0.42, y=10)

    Label(TravellerLoginPage, text='Username', bg='#f0f0f0', font=('arial', 20)).place(relx=0.3, rely=0.4)
    Label(TravellerLoginPage, text='Password', bg='#f0f0f0', font=('arial', 20)).place(relx=0.3, rely=0.5)
    
    
    TravellerUsername = ttk.Entry(TravellerLoginPage, font=('arial', 20))
    TravellerUsername.place(relx=0.5, rely=0.4)
    TravellerPassword = ttk.Entry(TravellerLoginPage, font=('arial', 20), show='*')
    TravellerPassword.place(relx=0.5, rely=0.5)
    
    Button(TravellerLoginPage, text ='LOGIN', padx=100, pady=5, font=('arial', 20, 'bold'), bg='#00ff99', fg='#f0f0f0', command=TravellerLogin).place(relx=0.39, y=500)

def TravellerHome(username):
    global TravellerHomePage
    TravellerHomePage = Tk()
    TravellerHomePage.iconbitmap('assets/bus.ico')
    TravellerHomePage.geometry('%dx%d+0+0' % (width, height))
    TravellerHomePage.title('Traveller Home')
    TravellerHomePage.config(bg='#f0f0f0')
    Frame(TravellerHomePage, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(TravellerHomePage, text=str(username) + '\'s Home', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.42, y=15)
    
    Button(TravellerHomePage, text='Book a Ticket', font=('Arial Black', 10), width=50, height=30, bg='#00ff99', fg='#f0f0f0', bd=6,
            command=NewBooking).place(relx=0.03, rely=0.2)

    Button(TravellerHomePage, text='Check Ticket Status', font=('Arial Black', 10), width=50, height=30, bg='#00ff99', fg='#f0f0f0', bd=6,
            command=CheckStatus).place(relx=0.35, rely=0.2)

    Button(TravellerHomePage, text='Update Your Details', font=('Arial Black', 10), width=50, height=30, bg='#00ff99', fg='#f0f0f0', bd=6,
            command=UpdateDetails).place(relx=0.67, rely=0.2)

def NewBooking():
    global BookingPage
    BookingPage = Tk()
    BookingPage.iconbitmap('assets/bus.ico')
    BookingPage.geometry('%dx%d+0+0' % (width, height))
    BookingPage.resizable(True,True)
    BookingPage.title('Ticket Booking')
    BookingPage.config(bg='#f0f0f0')
    Frame(BookingPage, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(BookingPage, text='Ticket Booking', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.42, y=15)

    global dep_from
    global dep_to
    global dep_date
    global meal
    
    MealOptions = ['veg', 'non-veg']
    Label(BookingPage, text='Departure From', font=('Helvetica', 10, 'bold'), bg='#f0f0f0').place(relx=0.29, y=180)
    Label(BookingPage, text='Departure To', font=('Helvetica', 10, 'bold'), bg='#f0f0f0').place(relx=0.29, y=215)
    Label(BookingPage, text='Date(YYYY-MM-DD)', font=('Helvetica', 10, 'bold'), bg='#f0f0f0').place(relx=0.29, y=250)
    Label(BookingPage, text='Meal', font=('Helvetica', 10, 'bold'), bg='#f0f0f0').place(relx=0.29, y=285)

    dep_from = ttk.Entry(BookingPage, width=30)
    dep_from.place(relx=0.4, y=180)
    
    dep_to = ttk.Entry(BookingPage, width=30)
    dep_to.place(relx=0.4, y=215)
    
    dep_date = ttk.Entry(BookingPage, width = 15)
    dep_date.place(relx=0.4, y=250)
    
    meal = StringVar(BookingPage)
    meal.set(MealOptions[0])
    OptionMenu(BookingPage, meal, *MealOptions).place(relx=0.4, y=285)

    ttk.Button(BookingPage, text='BOOK TICKET', width=20, command=BookTicket).place(relx=0.36, y=350)
    ttk.Button(BookingPage, text='EXIT', width=20, command=ExitBooking).place(relx=0.36, y=380)

def BookTicket():
    if dep_from.get() == '' or dep_to.get() == '' or dep_date.get() == '' or meal.get() == '':
        messagebox.showinfo('Required!', 'Please enter all values...')
        print('Booking Failed: All values not entered...')
    connection, cursor = ConnectDB()
    global tkt_no
    cursor.execute('''select tkt_no from booking order by tkt_no;''')
    tkt_no = cursor.fetchall()[0][-1]
    if tkt_no == None:
        tkt_no = 1000000000
    else:
        tkt_no = int(tkt_no[0]) + 1
    buses = []
    cursor.execute('select bus_id from buses;')
    for bus in cursor.fetchall():
        buses.append(bus[0])
    bus_id = random.choice(buses)
    seat_no = random.randint(1, 60)
    price = random.randint(300, 601)

    try:
        cursor.execute('''insert into booking values('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {});'''.format(str(tkt_no), username,
                    dep_from.get(), dep_to.get(), dep_date.get(), meal.get(), seat_no, bus_id, price))
        status = random.choice(['Confirmed', 'Waiting'])
        cursor.execute('''insert into tkt_status values('{}', '{}');'''.format(str(tkt_no), status))
        BookingPage.destroy()
        messagebox.showinfo('Success!', 'Booking completed successfully...')
        print('Booking successful...')
    except:
        print('Booking failed...')
        messagebox.showinfo('Error', 'Booking Failed')
    connection.commit()
    connection.close()

def ExitBooking():
    BookingPage.destroy()

def CheckStatus():
    global StatusPage
    StatusPage = Tk()
    StatusPage.iconbitmap('assets/bus.ico')
    StatusPage.geometry('%dx%d+0+0' % (width, height))
    StatusPage.resizable(True, True)
    StatusPage.title('Ticket Status')
    StatusPage.config(bg='#f0f0f0')
    Frame(StatusPage, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(StatusPage, text='Check Ticket Status', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.38, y=15)

    global tkt_no

    Label(StatusPage, text='Ticket Number', font=('Helvetica', 8, 'bold'), bg='#f0f0f0').place(relx=0.37, rely=0.3)
    tkt_no = ttk.Entry(StatusPage, width=15)
    tkt_no.place(relx=0.44, rely=0.3)

    Button(StatusPage, text='CHECK STATUS', font=('Arial Black', 10), bg='#00ff99', fg='#f0f0f0', command=GetStatus, width=15).place(relx=0.4, rely=0.35)
    Button(StatusPage, text='EXIT', font=('Arial Black', 10), bg='#00ff99', fg='#f0f0f0', command=ExitStatus, width=15).place(relx=0.4, rely=0.39)

    StatusPage.Right = ttk.Frame(StatusPage, width=width, height=10)
    StatusPage.Right.place(relx=0, rely=0.7)

    global TicketDetails

    scrollbarx = Scrollbar(StatusPage.Right, orient=VERTICAL)
    scrollbary = Scrollbar(StatusPage.Right, orient=HORIZONTAL)

    TicketDetails = ttk.Treeview(StatusPage.Right, columns=('tkt_no', 'username', 'fname', 'lname', 'dep_from',
                                    'dep_to', 'dep_date', 'meal', 'seat_no', 'bus_id', 'price', 'status'))
    
    scrollbary.config(command=TicketDetails.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=TicketDetails.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    TicketDetails.heading('tkt_no', text='Ticket Number', anchor=W)
    TicketDetails.heading('username', text='Username', anchor=W)
    TicketDetails.heading('fname', text='First Name', anchor=W)
    TicketDetails.heading('lname', text='Last Name', anchor=W)
    TicketDetails.heading('dep_from', text='Departure from', anchor=W)
    TicketDetails.heading('dep_to', text='Departure to', anchor=W)
    TicketDetails.heading('dep_date', text='Departure Date', anchor=W)
    TicketDetails.heading('meal', text='Meal', anchor=W)
    TicketDetails.heading('seat_no', text='Seat Number', anchor=W)
    TicketDetails.heading('bus_id', text='Bus Number', anchor=W)
    TicketDetails.heading('price', text='Price', anchor=W)
    TicketDetails.heading('status', text='Status', anchor=W)

    TicketDetails.column('#0', stretch=NO, minwidth=0, width=0)
    TicketDetails.column('#1', stretch=NO, minwidth=0, width=120)
    TicketDetails.column('#2', stretch=NO, minwidth=0, width=120)
    TicketDetails.column('#3', stretch=NO, minwidth=0, width=120)
    TicketDetails.column('#4', stretch=NO, minwidth=0, width=120)
    TicketDetails.column('#5', stretch=NO, minwidth=0, width=120)
    TicketDetails.column('#6', stretch=NO, minwidth=0, width=120)
    TicketDetails.column('#7', stretch=NO, minwidth=0, width=90)
    TicketDetails.column('#8', stretch=NO, minwidth=0, width=90)
    TicketDetails.column('#9', stretch=NO, minwidth=0, width=80)
    TicketDetails.column('#10', stretch=NO, minwidth=0, width=90)
    TicketDetails.column('#11', stretch=NO, minwidth=0, width=90)

    TicketDetails.pack()

def GetStatus():
    connection, cursor = ConnectDB()
    try:
        cursor.execute('''select status from tkt_status where tkt_no='{}';'''.format(tkt_no.get()))
        status = cursor.fetchone()[0]
        cursor.execute('''select * from booking where tkt_no='{}';'''.format(tkt_no.get()))
        res = cursor.fetchall()
        cursor.execute('''select fname, lname from customer where username='{}';'''.format(res[0][1]))
        x = cursor.fetchall()[0]
        fname = x[0]
        lname = x[1]
        for data in res:
            TicketDetails.insert('', 'end', values=(data[0], data[1], fname, lname, data[2], data[3], data[4], data[5],
                                data[6], data[7], data[8], status))
        connection.close()
        print('Ticket details found...')
    except:
        StatusPage.destroy()
        messagebox.showinfo('Error!', 'Record not found...')
        print('Ticket details not found...')

def ExitStatus():
    StatusPage.destroy()

def UpdateDetails():
    global UpdateDetailsPage
    UpdateDetailsPage = Tk()
    UpdateDetailsPage.iconbitmap('assets/bus.ico')
    UpdateDetailsPage.geometry('%dx%d+0+0' % (width, height))
    UpdateDetailsPage.title('Update User Details')
    UpdateDetailsPage.config(bg='#f0f0f0')
    Frame(UpdateDetailsPage, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(UpdateDetailsPage, text='Update User Details(any 1 field at a time)', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.26, y=15)
    
    global username
    global password
    global email
    global age
    global fname
    global lname
    global phone

    Label(UpdateDetailsPage, text='Password', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=205)
    Label(UpdateDetailsPage, text='Email', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=240)
    Label(UpdateDetailsPage, text='Age', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=275)
    Label(UpdateDetailsPage, text='First Name', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=310)
    Label(UpdateDetailsPage, text='Last Name', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=345)
    Label(UpdateDetailsPage, text='Phone Number', font=('helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=380)

    password = ttk.Entry(UpdateDetailsPage, width=30, show='*')
    password.place(relx=0.5, y=205)
    
    email = ttk.Entry(UpdateDetailsPage, width=30)
    email.place(relx=0.5, y=240)

    age = ttk.Entry(UpdateDetailsPage, width=30)
    age.place(relx=0.5, y=275)

    fname = ttk.Entry(UpdateDetailsPage, width=30)
    fname.place(relx=0.5, y=310)

    lname = ttk.Entry(UpdateDetailsPage, width=30)
    lname.place(relx=0.5, y=345)

    phone = ttk.Entry(UpdateDetailsPage, width=30)
    phone.place(relx=0.5, y=380)

    Button(UpdateDetailsPage, text='UPDATE', command=UpdateUser, font=('Arial', 10, 'bold'), width=20, bg='#00ff99', fg='#f0f0f0').place(relx=0.42, y=440)
    Button(UpdateDetailsPage, text='EXIT', command=ExitUpdateUser, font=('Arial', 10, 'bold'), width=20, bg='#00ff99', fg='#f0f0f0').place(relx=0.42, y=490)

def UpdateUser():
    connection, cursor = ConnectDB()
    try:
        if len(password.get()):
            cursor.execute('''update customer set password='{}' where username='{}';'''.format(password.get(), username))
        elif len(email.get()):
            cursor.execute('''update customer set email='{}' where username='{}';'''.format(email.get(), username))
        elif len(age.get()):
            cursor.execute('''update customer set age={} where username='{}';'''.format(age.get(), username))
        elif len(fname.get()):
            cursor.execute('''update customer set fname='{}' where username='{}';'''.format(fname.get(), username))
        elif len(lname.get()):
            cursor.execute('''update customer set lname='{}' where username='{}';'''.format(lname.get(), username))
        elif len(phone.get()):
            cursor.execute('''update customer set phone='{}' where username='{}';'''.format(phone.get(), username))
        else:
            print('Error: No value entered...')
            raise ValueError
        connection.commit()
        UpdateDetailsPage.destroy()
        messagebox.showinfo('Success!', 'Updated...')
        print('Success! Updated details...')
    except:
        UpdateDetailsPage.destroy()
        messagebox.showinfo('Error!', 'Failed...')
        print('Error! Could not update details')
    connection.close()

def ExitUpdateUser():
    UpdateDetailsPage.destroy()

def RegisterUser():
    global NewUserPage
    NewUserPage = Tk()
    NewUserPage.iconbitmap('assets/bus.ico')
    NewUserPage.geometry('%dx%d+0+0' % (width, height))
    NewUserPage.resizable(True, True)
    NewUserPage.title('Register User')
    NewUserPage.config(bg='#f0f0f0')
    Frame(NewUserPage, height=70, width=width, bg='#00ff99').place(relx=0, y=0)
    Label(NewUserPage, text='Register New User', font=('impact', 30, 'bold'), bg='#00ff99').place(relx=0.4, y=15)

    global username
    global password
    global email
    global age
    global fname
    global lname
    global phone

    Label(NewUserPage, text='Username', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=170)
    Label(NewUserPage, text='Password', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=205)
    Label(NewUserPage, text='Email', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=240)
    Label(NewUserPage, text='Age', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=275)
    Label(NewUserPage, text='First Name', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=310)
    Label(NewUserPage, text='Last Name', font=('Helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=345)
    Label(NewUserPage, text='Phone Number', font=('helvetica', 14, 'bold'), bg='#f0f0f0').place(relx=0.35, y=380)

    username = ttk.Entry(NewUserPage, width=30)
    username.place(relx=0.5, y=170)

    password = ttk.Entry(NewUserPage, width=30, show='*')
    password.place(relx=0.5, y=205)
    
    email = ttk.Entry(NewUserPage, width=30)
    email.place(relx=0.5, y=240)

    age = ttk.Entry(NewUserPage, width=30)
    age.place(relx=0.5, y=275)

    fname = ttk.Entry(NewUserPage, width=30)
    fname.place(relx=0.5, y=310)

    lname = ttk.Entry(NewUserPage, width=30)
    lname.place(relx=0.5, y=345)

    phone = ttk.Entry(NewUserPage, width=30)
    phone.place(relx=0.5, y=380)

    Button(NewUserPage, text='REGISTER', command=AddUser, font=('Arial', 10, 'bold'), width=20, bg='#00ff99', fg='#f0f0f0').place(relx=0.42, y=440)
    Button(NewUserPage, text='EXIT', command=ExitNewUser, font=('Arial', 10, 'bold'), width=20, bg='#00ff99', fg='#f0f0f0').place(relx=0.42, y=490)

def AddUser():
    if username.get() == '' or password.get() == '' or email.get() == '' or age.get() == '' or fname.get == '' or lname.get() == '' or phone.get() == '':
        messagebox.showinfo('Required!', 'Please enter all the values...')
        print('Error: all values not entered...')
    connection, cursor = ConnectDB()
    cursor.execute('''select username from customer where username='{}';'''.format(username))
    if cursor.fetchone() != None:
        messagebox.showinfo('Error!', 'Username already exists...')
        print('Username already exists...')
    try:
        cursor.execute('''insert into customer values('{}', '{}', '{}', {}, '{}', '{}', '{}');'''.format(username.get(), password.get(),
                        email.get(), age.get(), fname.get(), lname.get(), phone.get()))
        connection.commit()
        connection.close()
        NewUserPage.destroy()
        messagebox.showinfo('Successful!', 'Registered Successfully...')
        print('Registration successful...')
    except:
        NewUserPage.destroy()
        messagebox.showinfo('Error!', 'Registration Failed...')

def ExitNewUser():
    NewUserPage.destroy()

