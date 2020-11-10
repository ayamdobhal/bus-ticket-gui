def TravellerLogin():
    username = TravellerUsername.get()
    password = TravellerPassword.get()
    print('Username:', username)
    print('Password:', password)

    CURSOR.execute('''select username from customer where username='{}';'''.format(username))
    if not len(CURSOR.fetchone()):
        TravellerLogin.destroy()
        messagebox.showinfo('Error!', 'Provided username not found in the database.')
        return 
    CURSOR.execute('''select password from customer where username='{}';'''.format(username))
    if CURSOR.fetchall()[0][1] != password:
        TravellerLogin.destroy()
        messagebox.showinfo('Error!', 'Incorrect password.')
        return
    GoToTravellerHome()

def TravellerLoginWindow():
    global TravellerLoginPage
    global TravellerUsername
    global TravellerPassword
    TravellerLoginPage = Tk()
    TravellerLoginPage.title('Traveller Login')
    TravellerLoginPage.resizable(True, True)
    TravellerLoginPage.config(bg='#f2ecda')
    frame1 = Frame(TravellerLoginPage, height=50, width=1200, bg='#00ff99').place(relx=0, y=30)
    frame2 = Frame(TravellerLoginPage, height=80, width=1200, bg='#f0f0f0').place(x=0, y=90)
    label = Label(TravellerLoginPage, font=('times new roman', 30, 'bold'), text = 'Traveller Login').place(relx=0.4, y=100)
    TravellerLoginUsername = Label(TravellerLoginPage, text='traveller name', bg='#f0f0f0', font=('arial', 20, 'bold')).place(relx=380, y=356)
    TravellerUsername = ttk.Entry(TravellerLoginPage, font=('arial', 20))
    TravellerLoginPassword = Label(TravellerLoginPage, text='password', bg='#f0f0f0', font=('arial', 20)).place(x=380, y=410)
    TravellerPassword = ttk.Entry(TravellerLoginPage, font=('arial', 20), show='*')
    TravellerLoginPage = Button(TravellerLoginPage, text ='login', padx=100, pady=5, font=('arial', 20, 'bold'), bg='#00ff99', fg='#f0f0f0', command=AdminLogin).place(relx=0.39, y=470)
    TravellerLoginUsername.place(relx=0.5, rely=0.5)
    TravellerLoginPassword.place(x=639, y=410)

