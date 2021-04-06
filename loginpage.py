import tkinter

from menu import *

#root=login page
#root1=menu
#rootp=patient form

#variables
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
guest=None
#command for login button
def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='v' and S2=='1'):
        menu()
    elif(S1=='vivek' and S2=='abcd'):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font="bold")
        error.pack()
def appoint():
    global guest
    func()

#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,guest,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("280x250")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO UK NURSING",bg='white',fg='orange',font='Times 16 bold italic')
    username=tkinter.Label(topframe,text="USERNAME")
    userbox = tkinter.Entry(topframe)
    password=tkinter.Label(bottomframe,text="PASSWORD")
    passbox = tkinter.Entry(bottomframe,show="*")
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET,font="arial 8 bold")
    guest = tkinter.Button(bottomframe, text="GUEST LOGIN", command=appoint,font="arial 8 bold")
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    guest.pack()
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()

