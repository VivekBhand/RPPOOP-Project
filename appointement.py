from tkinter import *
import sqlite3

global root3
root3 = Tk()
root3.geometry("600x800+600+0")
root3.title("RECORDS")

Fullname = StringVar()
Mobileno = StringVar()
Email = StringVar()
Aadhar = StringVar()
Date = StringVar()
Age = StringVar()
var = IntVar()
Symptoms = IntVar()
Vaccine = IntVar()
s = StringVar()
c = StringVar()

def exit():
    global root3
    root3.destroy()
def database():
    name1 = Fullname.get()
    mobileno = Mobileno.get()
    email = Email.get()
    aadhar = Aadhar.get()
    date = Date.get()
    age = Age.get()
    gender = var.get()
    symptoms = Symptoms.get()
    vaccine = Vaccine.get()
    slot = s.get()
    city = c.get()
    conn = sqlite3.connect('PATIENT APPOINTMENT RECORDS.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Patient (Fullname TEXT,Mobileno TEXT,Email TEXT,Aadhar TEXT,Date TEXT,Age TEXT,Gender TEXT,Symptoms TEXT,Vaccine TEXT,Slot TEXT,City TEXT)')
    cursor.execute(
        'INSERT INTO Patient (FullName,Mobileno,Email,Aadhar,Date,Age,Gender,Symptoms,Vaccine,Slot,City) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
        (name1, mobileno, email, aadhar, date, age, gender, symptoms, vaccine, slot, city,))
    conn.commit()


Employeename = StringVar()
Employeeid = StringVar()
Mobileno = StringVar()
Email = StringVar()
Aadhar = StringVar()
Age = StringVar()
Salary = StringVar()
var = IntVar()
s = StringVar()


def edatabase():
    employeename = Employeename.get()
    employeeid = Employeeid.get()
    mobile = Mobileno.get()
    email = Email.get()
    aadhar = Aadhar.get()
    age = Age.get()
    salary = Salary.get()
    gender = var.get()
    employeetype = s.get()
    conn = sqlite3.connect('EMPLOYEE APPOINTMENT RECORDS.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Employee (Employeename TEXT,Employeeid TEXT,Mobileno TEXT,Email TEXT,Aadhar TEXT,Age TEXT,Salary TEXT,Gender TEXT,Employeetype TEXT)')
    cursor.execute(
        'INSERT INTO Employee (Employeename,Employeeid,Mobileno,Email,Aadhar,Age,Salary,Gender,Employeetype) VALUES(?,?,?,?,?,?,?,?,?)',
        (employeename, employeeid, mobile, email, aadhar, age, salary, gender, employeetype,))
    conn.commit()


def func():
    label_0 = Label(root3, text="PATIENT APPOINTMENT RECORDS", fg='red', width=0, font=("bold", 15))
    label_0.place(x=90, y=53)

    label_1 = Label(root3, text="ENTER FULL NAME", width=20, font=("bold", 9))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root3, textvar=Fullname)
    entry_1.place(x=240, y=130)

    label_2 = Label(root3, text="ENTER MOBILE NO.", width=20, font=("bold", 9))
    label_2.place(x=80, y=155)

    entry_2 = Entry(root3, textvar=Mobileno)
    entry_2.place(x=240, y=155)

    label_3 = Label(root3, text="ENTER EMAIL ID.", width=20, font=("bold", 9))
    label_3.place(x=80, y=180)

    entry_3 = Entry(root3, textvar=Email)
    entry_3.place(x=240, y=180)

    label_4 = Label(root3, text="ENTER AADHAR NO.", width=20, font=("bold", 9))
    label_4.place(x=80, y=205)

    entry_4 = Entry(root3, textvar=Aadhar)
    entry_4.place(x=240, y=205)

    label_4 = Label(root3, text="ENTER DATE", width=20, font=("bold", 9))
    label_4.place(x=80, y=230)

    entry_4 = Entry(root3, textvar=Date)
    entry_4.place(x=240, y=230)

    label_5 = Label(root3, text="AGE OF PATIENT", width=20, font=("bold", 9))
    label_5.place(x=80, y=255)

    entry_5 = Entry(root3, textvar=Age)
    entry_5.place(x=240, y=255)

    label_6 = Label(root3, text="SELECT GENDER", width=20, font=("bold", 9))
    label_6.place(x=80, y=280)

    r1 = Radiobutton(root3, text="MALE", padx=10, variable=var, value=1)
    r1.place(x=235, y=280)
    r2 = Radiobutton(root3, text="FEMALE", padx=30, variable=var, value=2)
    r2.place(x=300, y=280)

    label_7 = Label(root3, text=" COVID SYMPOTMS?", width=20, font=("bold", 9))
    label_7.place(x=80, y=305)

    r3 = Radiobutton(root3, text="YES", padx=10, variable=Symptoms, value=1)
    r3.place(x=235, y=305)
    r4 = Radiobutton(root3, text="NO", padx=30, variable=Symptoms, value=2)
    r4.place(x=300, y=305)

    label_8 = Label(root3, text="COVID VACCINE?", width=20, font=("bold", 9))
    label_8.place(x=80, y=330)

    r5 = Radiobutton(root3, text="YES", padx=10, variable=Vaccine, value=1)
    r5.place(x=235, y=330)
    r6 = Radiobutton(root3, text="NO", padx=30, variable=Vaccine, value=2)
    r6.place(x=300, y=330)

    label_9 = Label(root3, text="SELECT SLOT", width=20, font=("bold", 9))
    label_9.place(x=70, y=355)

    list1 = ['10.00-11.00am', '11.00-12.00am', '12.15-01.15pm', '01.15-02.15pm', '06.00-07.00pm', '07.00-08.00pm'];

    droplist = OptionMenu(root3, s, *list1)
    droplist.config(bg='yellow', fg='black', width=15)
    s.set('Select your slot')
    droplist.place(x=240, y=355)

    label_10 = Label(root3, text="SELECT CITY", width=20, font=("bold", 9))
    label_10.place(x=70, y=380)

    list2 = ['Kalyan', 'Ulhasnagar', 'Thane', 'Dombivali', 'Mumbai', 'Shivajinagar'];

    droplist = OptionMenu(root3, c, *list2)
    droplist.config(bg='yellow', fg='black', width=15)
    c.set('Select your city')
    droplist.place(x=240, y=380)

    """label_6 = Label(root3, text="ENTER UNIQUE ID", width=20, font=("bold", 9))
    label_6.place(x=80, y=400)

    entry_6 = Entry(root3, textvar=UID)
    entry_6.place(x=240, y=420)
    """

    Button(root3, text='Submit', width=20, bg='green', fg='black', command=database).place(x=180, y=440)
    Button(root3, text='Exit', width=10, bg='green', fg='black', command=exit).place(x=220, y=480)
    root3.mainloop()


def reg():
    label_0 = Label(root3, text="EMPLOYEE APPOINTMENT RECORDS", fg='red', width=0, font=("bold", 15))
    label_0.place(x=90, y=53)

    label_1 = Label(root3, text="ENTER EMPLOYEE NAME", width=20, font=("bold", 9))
    label_1.place(x=80, y=130)

    entry_1 = Entry(root3, textvar=Employeename)
    entry_1.place(x=240, y=130)

    label_2 = Label(root3, text="ENTER EMPLOYEE ID", width=20, font=("bold", 9))
    label_2.place(x=80, y=155)

    entry_2 = Entry(root3, textvar=Employeeid)
    entry_2.place(x=240, y=155)

    label_3 = Label(root3, text="ENTER MOBILE NO.", width=20, font=("bold", 9))
    label_3.place(x=80, y=180)

    entry_3 = Entry(root3, textvar=Mobileno)
    entry_3.place(x=240, y=180)

    label_4 = Label(root3, text="ENTER EMAIL", width=20, font=("bold", 9))
    label_4.place(x=80, y=205)

    entry_4 = Entry(root3, textvar=Email)
    entry_4.place(x=240, y=205)

    label_5 = Label(root3, text="ENTER AADHAR NO.", width=20, font=("bold", 9))
    label_5.place(x=80, y=230)

    entry_5 = Entry(root3, textvar=Aadhar)
    entry_5.place(x=240, y=230)

    label_6 = Label(root3, text="AGE", width=20, font=("bold", 9))
    label_6.place(x=80, y=255)

    entry_6 = Entry(root3, textvar=Age)
    entry_6.place(x=240, y=255)

    label_7 = Label(root3, text="SALARY", width=20, font=("bold", 9))
    label_7.place(x=80, y=280)

    entry_7 = Entry(root3, textvar=Salary)
    entry_7.place(x=240, y=280)

    label_8 = Label(root3, text="SELECT GENDER", width=20, font=("bold", 9))
    label_8.place(x=80, y=305)

    r1 = Radiobutton(root3, text="MALE", padx=5, variable=var, value=1)
    r1.place(x=235, y=305)
    r2 = Radiobutton(root3, text="FEMALE", padx=20, variable=var, value=2)
    r2.place(x=300, y=305)

    label_9 = Label(root3, text="SELECT EMPLOYEE TYPE", width=20, font=("bold", 9))
    label_9.place(x=70, y=330)

    list12 = ['Doctor', 'Nurse', 'Floor sweeper'];

    droplist = OptionMenu(root3, s, *list12)
    droplist.config(bg='yellow', fg='black', width=15)
    s.set('Select Employee Type')
    droplist.place(x=240, y=330)

    Button(root3, text='Submit', width=20, bg='green', fg='black', command=edatabase).place(x=180, y=440)
    Button(root3, text='Exit', width=10, bg='green', fg='black', command=exit).place(x=220, y=480)

    root3.mainloop()


