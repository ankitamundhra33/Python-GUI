from tkinter import *
import os
creds='credss.temp'


def signup():
    global password
    global username
    global root

    root=Tk()
    root.title('Signup')
    instructs=Label(root,text='Please enter your username and password\n')
    instructs.grid(row=0,column=0,sticky=E)
    username=Label(root,text='Username')
    password=Label(root,text='Password')
    username.grid(row=1,column=0,sticky=W)
    password.grid(row=2,column=0,sticky=W)

    username=Entry(root)
    password=Entry(root,show='*')
    username.grid(row=1, column=1)
    password.grid(row=2, column=1)

    signupBtn=Button(root,text='SignUp',command=fsignUp)
    signupBtn.grid(columnspan=2,sticky=W)
    root.mainloop()


def fsignUp():
    with open(creds,'w') as f:
        f.write(username.get())
        f.write('\n')
        f.write(password.get())
        f.close()
    root.destroy()
    login()


def login():
    global name
    global passw
    global roots

    roots=Tk()
    roots.title('Login')
    instructs = Label(roots, text='Login\n')
    instructs.grid(row=0, column=0, sticky=E)
    name = Label(roots, text='Username')
    passw = Label(roots, text='Password')
    name.grid(row=1, column=0, sticky=W)
    passw.grid(row=2, column=0, sticky=W)

    name = Entry(roots)
    passw = Entry(roots, show='*')
    name.grid(row=1, column=1)
    passw.grid(row=2, column=1)

    loginBtn = Button(roots, text='Login', command=checkLogin)
    loginBtn.grid(columnspan=2, sticky=W)
    signup1=Button(roots, text='SignUp',command=signup)
    signup1.grid(columnspan=2,sticky=W)
    user=Button(roots,text='Delete User',fg='blue',command=Deluser)
    user.grid(columnspan=2,sticky=W)
    roots.mainloop()


def checkLogin():
    with open(creds) as f:
        data=f.readlines()
        uname=data[0].rstrip()
        pwd=data[1].rstrip()

    if name.get()==uname and passw.get()==pwd:
        r=Tk()
        r.title('Login Page')
        r.geometry('400x400')
        rlbl=Label(r,text='\n[+] Logged In')
        rlbl.pack()
        r.mainloop()
    else:
        r=Tk()
        r.title('Login Checked')
        r.geometry('400x400')
        rlbl = Label(r, text='\n[+] Invalid Login')
        rlbl.pack()
        r.mainloop()


def Deluser():
    os.remove(creds)
    roots.destroy()
    signup()
if os.path.isfile(creds):
    login()
else:
    signup()