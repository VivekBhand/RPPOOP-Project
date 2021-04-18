import tkinter
import sqlite3
import tkinter.messagebox
from registration import *
from delete import *

#variables
root1=None
rootp=None
pat_ID=None
pat_name=None
pat_dob=None
pat_address=None
pat_sex=None
pat_BG=None
pat_email=None
pat_contact=None
pat_contactalt=None
pat_CT=None

#EXIT for MENU
def ex():
    global root1
    root1.destroy()



def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    root1.geometry("400x350")
    root1.title("MAIN MENU")
    m=tkinter.Label(root1,text="MENU",font='Times 16 bold italic',fg='grey')
    button1=tkinter.Button(root1,text="1. BOOK APPOINTMENT",command=func,bg='light blue',fg='black')
    button2 = tkinter.Button(root1, text="2.VIEW APPOINTEMENT",command=func,bg='light green',fg='black')
    button3 = tkinter.Button(root1, text="3.EMPLOYEE REGISTRATION",command=reg,bg='light blue',fg='black')
    button4 = tkinter.Button(root1, text="4.DELETE APPOINTMENT",command=submit,bg='light green',fg='black')
    #button5 = tkinter.Button(root1, text="5.PATIENT BILL",bg='light blue',fg='black')
    button6 = tkinter.Button(root1, text="5.EXIT",command=ex,bg='light green',fg='black')
    m.place(x=75,y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80,y=50)
    button2.pack(side=tkinter.TOP)
    button2.place(x=80,y=100)
    button3.pack(side=tkinter.TOP)
    button3.place(x=80,y=150)
    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=200)
    #button5.pack(side=tkinter.TOP)
    #button5.place(x=80,y=250)
    button6.pack(side=tkinter.TOP)
    button6.place(x=80,y=250)
    root1.mainloop()

