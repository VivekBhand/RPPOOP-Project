import tkinter
import sqlite3
import tkinter.messagebox
from appointement import *
from update import *
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
window=None

#EXIT for MENU
def ex():
    global root1
    root1.destroy()



def menu():
    global root1,button1,button2,button3,button4,button5,m,button6
    root1=tkinter.Tk()
    root1.geometry("800x720+0+0")
    root1.title("MAIN MENU")
    m=tkinter.Label(root1,text="MENU",font='Times 16 bold italic',fg='grey')
    button1=tkinter.Button(root1,text="1. BOOK APPOINTMENT",command=func,bg='light blue',fg='black')
    
    button3 = tkinter.Button(root1, text="2.EMPLOYEE REGISTRATION",command=reg,bg='light blue',fg='black')
    button4 = tkinter.Button(root1, text="3.DELETE or UPDATE APPOINTMENT",command=func4,bg='light green',fg='black')
    
    button6 = tkinter.Button(root1, text="4.EXIT",command=ex,bg='light green',fg='black')
    m.place(x=75,y=5)
    button1.pack(side=tkinter.TOP)
    button1.place(x=80,y=50)
    button3.pack(side=tkinter.TOP)
    button3.place(x=80,y=100)
    button4.pack(side=tkinter.TOP)
    button4.place(x=80, y=150)
    button6.pack(side=tkinter.TOP)
    button6.place(x=80,y=200)
    root1.mainloop()

