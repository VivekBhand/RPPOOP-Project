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
        error=tkinter.Label(bottomframe,text="\tWrong Id / Password TRY AGAIN",fg="red",font="bold")
        error.pack(side=tkinter.TOP)
        error.pack()
        #error.place(x=200,y=300)
    
def appoint():
    global guest
    func()

#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,guest,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("550x350")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(root, text="Welcome To UK Nursing",bg='white',fg='red',font='Times 20 bold italic')
    username=tkinter.Label(root,text="USERNAME")
    userbox = tkinter.Entry(root)
    password=tkinter.Label(root,text="PASSWORD")
    passbox = tkinter.Entry(root,show="*")
    login = tkinter.Button(root, text="LOGIN",bg='yellow', command=GET,font="arial 8 bold")
    guest = tkinter.Button(root, text="GUEST LOGIN",bg='yellow', command=appoint,font="arial 8 bold")
    heading.pack(side=tkinter.TOP)
    heading.place(x=155,y=30)
    username.pack(side=tkinter.TOP)
    username.place(x=185,y=100)
    userbox.pack(side=tkinter.TOP)
    userbox.place(x=285,y=100)
    password.pack(side=tkinter.TOP)
    password.place(x=185,y=140)
    passbox.pack(side=tkinter.TOP)
    passbox.place(x=285,y=140)
    login.pack(side=tkinter.TOP)
    login.place(x=245,y=180)
    
    guest.pack(side=tkinter.TOP)
    guest.place(x=235,y=220)
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()

