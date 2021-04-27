import tkinter
import sqlite3
import tkinter.messagebox
from appointement import *
from employee import *
from update import *


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
    button2 = tkinter.Button(root1, text="2.VIEW APPOINTMENTS",command=func4,bg='light green',fg='black')
    button3 = tkinter.Button(root1, text="3.EMPLOYEE REGISTRATION",command=reg,bg='light blue',fg='black')
    button4 = tkinter.Button(root1, text="4.VIEW EMPLOYEE RECORDS",command=func5,bg='light green',fg='black')
    #button5 = tkinter.Button(root1, text="5.SEARCH BY ADHAAR",command=submit_search,bg='light blue',fg='black')
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

