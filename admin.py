def AdminLogin():
    password = AdminPassword.get()
    print('Password:', password)
    if password = 'admin':
        GoToAdminHome()

def AdminLoginWindow():
    global AdminLoginPage
    global AdminPassword
    AdminLoginPage = Tk()
    AdminLoginPage.title('Admin Login')
    AdminLoginPage.resizable(True, True)
    AdminLoginPage.config(bg='#f2ecda')
    frame1 = Frame(AdminLoginPage, height=50, width=1200, bg='#00ff99').place(relx=0, y=30)
    frame2 = Frame(AdminLoginPage, height=80, width=1200, bg='#f0f0f0').place(x=0, y=90)
    label = Label(AdminLoginPage, font=('times new roman', 30, 'bold'), text = 'Admin Login').place(relx=0.4, y=100)
    AdminLoginUsername = Label(AdminLoginPage, text='admin', bg='#f0f0f0', font=('arial', 20, 'bold')).place(relx=0.39, y=356)
    AdminLoginPassword = Label(AdminLoginPage, text='password', bg='#f0f0f0', font=('arial', 20)).place(x=380, y=410)
    AdminPassword = ttk.Entry(AdminPassword, font=('arial', 20), show='*')
    AdminLoginButton = Button(AdminLoginPage, text ='login', padx=100, pady=5, font=('arial', 20, 'bold'), bg='#00ff99', fg='#f0f0f0', command=AdminLogin).place(relx=0.39, y=470)
    AdminLoginPassword.place(x=639, y=410)
