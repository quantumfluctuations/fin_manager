from tkinter import *
from functools import partial
from tkinter import ttk

user = "admin"
passwd_admin = "admin"
user0 = "user"
psswd = "biabest"

monayy = []
reasons = []
    


def validateLogin(username, password):

    if username.get() == user and password.get() == passwd_admin:
        adminwindow()
    
    elif username.get() == user0 and password.get() == psswd:
        def data():
            stonk= entry.get()
            reason=entry1.get()
            monayy.append(stonk)
            reasons.append(reason)
                
        root = Tk()
        root.geometry('400x150')
        root.title('User')
        label=Label(root, text="Enter money spent(USD)")
        label.pack()
        global entry
        entry= Entry(root, width= 40)
        entry.focus_set()
        entry.pack()
        label1=Label(root,text="Reason")
        label1.pack()
        global entry1
        entry1 = Entry(root,width=40)
        entry1.focus_set()
        entry1.pack()
        ttk.Button(root, text= "Enter",width= 20, command= data).pack(pady=20)

    else:
        print("bruh")
    return


def adminwindow():

    tkWindow = Tk()

    tkWindow.geometry('400x150')

    tkWindow.title('Admin')
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(tkWindow, column=("Money Spent", "Reason"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Money spent")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Reason")
    for i in range(0,len(monayy),1):
        tree.insert('', 'end', text="1", values=(monayy[i], reasons[i]))
    tree.pack() 
    tkWindow.mainloop()

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Login')
usernameLabel = Label(tkWindow, text="Username").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password,show='*').grid(row=1, column=1)
validateLogin = partial(validateLogin, username, password)
loginButton = Button(tkWindow, text="Login",command=validateLogin).grid(row=4, column=0)
tkWindow.mainloop()
