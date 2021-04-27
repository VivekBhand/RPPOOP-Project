import tkinter

from menu import *
from covid import *

root = None
userbox = None
passbox = None
topframe = None
bottomframe = None
frame3 = None
login = None
guest = None


# command for login button
def GET():
    global userbox, passbox, error
    S1 = userbox.get()
    S2 = passbox.get()
    if (S1 == 'v' and S2 == '1'):
        menu()
    elif (S1 == 'vivek' and S2 == 'abcd'):
        menu()
    elif(S1 == 'vipul' and S2 == 'xyzw'):
        menu()
    elif(S1 == 'vipin' and S2 == 'qwer'):
        menu()
    else:
        error = tkinter.Label(bottomframe, text="\tWrong Id / Password TRY AGAIN", fg="red", font="bold")
        error.pack(side=tkinter.TOP)
        error.pack()
       


def appoint():
    global guest
    func()


def corona():
    global button
    openweb()


# LOGIN PAGE WINDOW
def Entry():
    global userbox, passbox, login, guest, topframe, bottomframe, image_1
    root = tkinter.Tk()
    root.geometry("800x720+0+0")
    root.config(bg='steelblue')
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe = tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(root, text="Welcome To Central Hospital", bg='steelblue', fg='black', font='Times 24')
    username = tkinter.Label(root, text="USERNAME")
    userbox = tkinter.Entry(root)
    password = tkinter.Label(root, text="PASSWORD")
    passbox = tkinter.Entry(root, show="*")
    login = tkinter.Button(root, text="LOGIN", bg='yellow', command=GET, font="arial 8 bold")
    guest = tkinter.Button(root, text="GUEST LOGIN", bg='yellow', command=appoint, font="arial 8 bold")
    button = tkinter.Button(root, text="COVID DATA", bg='yellow', command=corona, font="arial 8 bold")
    heading.pack(side=tkinter.TOP)
    heading.place(x=155, y=30)
    username.pack(side=tkinter.TOP)
    username.place(x=185, y=100)
    userbox.pack(side=tkinter.TOP)
    userbox.place(x=285, y=100)
    password.pack(side=tkinter.TOP)
    password.place(x=185, y=140)
    passbox.pack(side=tkinter.TOP)
    passbox.place(x=285, y=140)
    login.pack(side=tkinter.TOP)
    login.place(x=310, y=180)

    guest.pack(side=tkinter.TOP)
    guest.place(x=235, y=220)
    button.pack(side=tkinter.TOP)
    button.place(x=360, y=220)
    root.title("DATABASE LOGIN")
    root.mainloop()


Entry()


