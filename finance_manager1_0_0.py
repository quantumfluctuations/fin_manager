from tkinter import *
from functools import partial
from tkinter import ttk

#setting passwords for all users and also usernames
user = "admin"
passwd_admin = "admin"
user0 = "user"
psswd = "bia123"

# list of money and reasons 

money = []
reasons = []
    
# function for validating login and to check if username and password are correct 

def validateLogin(username, password):

    if username.get() == user and password.get() == passwd_admin:
        adminwindow()
    
    elif username.get() == user0 and password.get() == psswd:
        # function to store data of user , i.e. the money spent and reasons why user spent the money  
        def data():
            amount = entry.get()
            reason=entry1.get()
            money.append(amount)
            reasons.append(reason)

        # the below functions make the input field where the user can input the money that he spent        
        root = Tk()
        root.geometry('400x150')
        root.title('User')
        label=Label(root, text="Enter money spent( $ )") 
        label.pack()
        global entry                         # the global module makes it so that we can use the variables outside of the function
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
        print("Incorrect Username or Password") # if somone enters wrong password or username in the field it shows this error in the terminal
    return

# function for loading in admin page 

def adminwindow():
    
    # this is the admin window, where someone can see all the money spent and why it was spent    

    tkWindow = Tk()

    tkWindow.geometry('400x150')

    tkWindow.title('Admin window - January 2023')
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(tkWindow, column=("Money Spent", "Reason"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Money spent")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Reason")
    for i in range(0,len(money),1):
        tree.insert('', 'end', text="1", values=(money[i], reasons[i]))
    tree.pack() 
    tkWindow.mainloop()

# this is the basic login page and also creating the window and running the loop
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Login')

usernameLabel = Label(tkWindow, text="Username").grid(row=1, column=1)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=1, column=2)
passwordLabel = Label(tkWindow, text="Password").grid(row=2, column=1)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password,show='*').grid(row=2, column=2)
validateLogin = partial(validateLogin, username, password)
loginButton = Button(tkWindow, text="Login",command=validateLogin).grid(row=3, column=0)
tkWindow.mainloop() # the mainloop is where the code keeps looping to give us a smooth interface
