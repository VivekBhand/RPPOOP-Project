# -*- coding: utf-8 -*-
from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x600')
root.title("PATIENT APPOINTMENT RECORDS")

Fullname = StringVar()
Mobileno = StringVar()
Email = StringVar()
Aadhar = StringVar()
Age = StringVar()
var = IntVar()
Symptoms = IntVar()
Vaccine = IntVar()
s = StringVar()
c = StringVar()


def database():
    name1 = Fullname.get()
    mobileno = Mobileno.get()
    email = Email.get()
    aadhar = Aadhar.get()
    age = Age.get()
    gender = var.get()
    symptoms = Symptoms.get()
    vaccine = Vaccine.get()
    slot = s.get()
    city = c.get()
    conn = sqlite3.connect(' PATIENT APPOINTMENT RECORDS.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Patient (Fullname TEXT,Mobileno TEXT,Email TEXT,Aadhar TEXT,Age TEXT,Gender TEXT,Symptoms TEXT,Vaccine TEXT,Slot TEXT,City TEXT)')
    cursor.execute('INSERT INTO Patient (FullName,Mobileno,Email,Aadhar,Age,Gender,Symptoms,Vaccine,Slot,City) VALUES(?,?,?,?,?,?,?,?,?,?)',
                   (name1, mobileno, email, aadhar ,age, gender,symptoms,vaccine, slot, city,))
    conn.commit()

def clear_all():
	entry_1.delete(0,END)
	entry_2.delete(0,END)
	entry_3.delete(0,END)
	entry_4.delete(0,END)
	entry_5.delete(0,END)
	r1.deselect()
	r2.deselect()
	r3.deselect()
	r4.deselect() 
	r5.deselect()
	r6.deselect()


label_0 = Label(root, text="PATIENT APPOINTMENT RECORDS", fg='red', width=0, font=("bold", 15))
label_0.place(x=90, y=53)

label_1 = Label(root, text="ENTER FULL NAME", width=20, font=("bold", 9))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="ENTER MOBILE NO.", width=20, font=("bold", 9))
label_2.place(x=80, y=155)

entry_2 = Entry(root, textvar=Mobileno)
entry_2.place(x=240, y=155)

label_3 = Label(root, text="ENTER EMAIL ID.", width=20, font=("bold", 9))
label_3.place(x=80, y=180)

entry_3 = Entry(root, textvar=Email)
entry_3.place(x=240, y=180)

label_4 = Label(root, text="ENTER AADHAR NO.", width=20, font=("bold", 9))
label_4.place(x=80, y=205)

entry_4 = Entry(root, textvar=Aadhar)
entry_4.place(x=240, y=205)

label_5 = Label(root, text="AGE OF PATIENT", width=20, font=("bold", 9))
label_5.place(x=80, y=230)

entry_5 = Entry(root, textvar=Age)
entry_5.place(x=240, y=230)

label_6 = Label(root, text="SELECT GENDER", width=20, font=("bold", 9))
label_6.place(x=80, y=255)

r1 = Radiobutton(root, text="MALE", padx=5, variable=var, value=1)
r1.place(x=235, y=255)
r2 = Radiobutton(root, text="FEMALE", padx=20, variable=var, value=2)
r2.place(x=300, y=255)

label_7 = Label(root, text=" COVID SYMPOTMS?", width=20, font=("bold", 9))
label_7.place(x=80, y=280)

r3 = Radiobutton(root, text="YES", padx=5, variable=Symptoms, value=1)
r3.place(x=235, y=280)
r4 = Radiobutton(root, text="NO", padx=20, variable=Symptoms, value=2)
r4.place(x=300, y=280)

label_8 = Label(root, text="COVID VACCINE?", width=20, font=("bold", 9))
label_8.place(x=80, y=305)

r5 = Radiobutton(root, text="YES", padx=5, variable=Vaccine, value=1)
r5.place(x=235, y=305)
r6 = Radiobutton(root, text="NO", padx=20, variable=Vaccine, value=2)
r6.place(x=300, y=305)

label_9 = Label(root, text="SELECT SLOT", width=20, font=("bold", 9))
label_9.place(x=70, y=330)

list1 = ['10.00-11.00am', '11.00-12.00am', '12.15-01.15pm', '01.15-02.15pm', '06.00-07.00pm', '07.00-08.00pm'];

droplist = OptionMenu(root, s, *list1)
droplist.config(bg='yellow', fg='black', width=15)
s.set('Select your slot')
droplist.place(x=240, y=330)

label_10 = Label(root, text="SELECT CITY", width=20, font=("bold", 9))
label_10.place(x=70, y=355)

list2 = ['Kalyan', 'Ulhasnagar', 'Thane', 'Dombivali', 'Mumbai', 'Shivajinagar'];

droplist = OptionMenu(root, c, *list2)
droplist.config(bg='yellow', fg='black', width=15)
c.set('Select your city')
droplist.place(x=240, y=355)

Button(root, text='Submit', width=20, bg='green', fg='black', command=database).place(x=180, y=400)
Button(root, text='Next Entry', width=20, bg='green', fg='black', command=lambda:clear_all()).place(x=180, y=430)

root.mainloop()


