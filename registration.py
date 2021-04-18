from tkinter import *
import sqlite3

rootr = None
rootr = Tk()
rootr.geometry('500x600')
rootr.title("RECORDS")


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
    conn = sqlite3.connect('PATIENT APPOINTMENT RECORDS.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Patient (Fullname TEXT,Mobileno TEXT,Email TEXT,Aadhar TEXT,Age TEXT,Gender TEXT,Symptoms TEXT,Vaccine TEXT,Slot TEXT,City TEXT)')
    cursor.execute('INSERT INTO Patient (FullName,Mobileno,Email,Aadhar,Age,Gender,Symptoms,Vaccine,Slot,City) VALUES(?,?,?,?,?,?,?,?,?,?)',
                   (name1, mobileno, email, aadhar ,age, gender,symptoms,vaccine, slot, city,))
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
    cursor.execute('INSERT INTO Employee (Employeename,Employeeid,Mobileno,Email,Aadhar,Age,Salary,Gender,Employeetype) VALUES(?,?,?,?,?,?,?,?,?)',       
        (employeename, employeeid, mobile, email, aadhar, age, salary, gender, employeetype,))
    conn.commit()


def func():
	label_0 = Label(rootr, text="PATIENT APPOINTMENT RECORDS", fg='red', width=0, 		font=("bold", 15))
	label_0.place(x=90, y=53)
	

	label_1 = Label(rootr, text="ENTER FULL NAME", width=20, font=("bold", 9))
	label_1.place(x=80, y=130)
	
	entry_1 = Entry(rootr, textvar=Fullname)
	entry_1.place(x=240, y=130)
	
	label_2 = Label(rootr, text="ENTER MOBILE NO.", width=20, font=("bold", 9))
	label_2.place(x=80, y=155)
	
	entry_2 = Entry(rootr, textvar=Mobileno)
	entry_2.place(x=240, y=155)
	
	label_3 = Label(rootr, text="ENTER EMAIL ID.", width=20, font=("bold", 9))
	label_3.place(x=80, y=180)
	
	entry_3 = Entry(rootr, textvar=Email)
	entry_3.place(x=240, y=180)
		
	label_4 = Label(rootr, text="ENTER AADHAR NO.", width=20, font=("bold", 9))
	label_4.place(x=80, y=205)

	entry_4= Entry(rootr, textvar=Aadhar)
	entry_4.place(x=240, y=205)

	label_5 = Label(rootr, text="AGE OF PATIENT", width=20, font=("bold", 9))
	label_5.place(x=80, y=230)
	
	entry_5 = Entry(rootr, textvar=Age)
	entry_5.place(x=240, y=230)

	label_6 = Label(rootr, text="SELECT GENDER", width=20, font=("bold", 9))
	label_6.place(x=80, y=255)

	r1 = Radiobutton(rootr, text="MALE", padx=10, variable=var, value=1)
	r1.place(x=235, y=255)
	r2 = Radiobutton(rootr, text="FEMALE", padx=30, variable=var, value=2)
	r2.place(x=300, y=255)

	label_7 = Label(rootr, text=" COVID SYMPOTMS?", width=20, font=("bold", 9))
	label_7.place(x=80, y=280)

	r3 = Radiobutton(rootr, text="YES", padx=10, variable=Symptoms, value=1)
	r3.place(x=235, y=280)
	r4 = Radiobutton(rootr, text="NO", padx=30, variable=Symptoms, value=2)
	r4.place(x=300, y=280)

	label_8 = Label(rootr, text="COVID VACCINE?", width=20, font=("bold", 9))
	label_8.place(x=80, y=305)

	r5 = Radiobutton(rootr, text="YES", padx=10, variable=Vaccine, value=1)
	r5.place(x=235, y=305)
	r6 = Radiobutton(rootr, text="NO", padx=30, variable=Vaccine, value=2)
	r6.place(x=300, y=305)

	label_9 = Label(rootr, text="SELECT SLOT", width=20, font=("bold", 9))
	label_9.place(x=70, y=330)

	list1 = ['10.00-11.00am', '11.00-12.00am', '12.15-01.15pm', '01.15-02.15pm', '06.00-07.00pm', '07.00-08.00pm'];

	droplist = OptionMenu(rootr, s, *list1)
	droplist.config(bg='yellow', fg='black', width=15)
	s.set('Select your slot')
	droplist.place(x=240, y=330)

	label_10 = Label(rootr, text="SELECT CITY", width=20, font=("bold", 9))
	label_10.place(x=70, y=355)

	list2 = ['Kalyan', 'Ulhasnagar', 'Thane', 'Dombivali', 'Mumbai', 'Shivajinagar'];

	droplist = OptionMenu(rootr, c, *list2)
	droplist.config(bg='yellow', fg='black', width=15)
	c.set('Select your city')
	droplist.place(x=240, y=355)
	
	"""label_6 = Label(rootr, text="ENTER UNIQUE ID", width=20, font=("bold", 9))
	label_6.place(x=80, y=400)
	
	entry_6 = Entry(rootr, textvar=UID)
	entry_6.place(x=240, y=420)
	"""

	Button(rootr, text='Submit', width=20, bg='green', fg='black', command=database).place(x=180, y=440)


def reg():
	label_0 = Label(rootr, text="EMPLOYEE APPOINTMENT RECORDS", fg='red', width=0, 		font=("bold", 15))
	label_0.place(x=90, y=53)
	

	label_1 = Label(rootr, text="ENTER EMPLOYEE NAME", width=20, font=("bold", 9))
	label_1.place(x=80, y=130)
	
	entry_1 = Entry(rootr, textvar=Employeename)
	entry_1.place(x=240, y=130)
	
	label_2 = Label(rootr, text="ENTER EMPLOYEE ID", width=20, font=("bold", 9))
	label_2.place(x=80, y=155)
	
	entry_2 = Entry(rootr, textvar=Employeeid)
	entry_2.place(x=240, y=155)
	
	label_3 = Label(rootr, text="ENTER MOBILE NO.", width=20, font=("bold", 9))
	label_3.place(x=80, y=180)
	
	entry_3 = Entry(rootr, textvar=Mobileno)
	entry_3.place(x=240, y=180)
		
	label_4 = Label(rootr, text="ENTER EMAIL", width=20, font=("bold", 9))
	label_4.place(x=80, y=205)

	entry_4= Entry(rootr, textvar=Email)
	entry_4.place(x=240, y=205)

	label_5 = Label(rootr, text="ENTER AADHAR NO.", width=20, font=("bold", 9))
	label_5.place(x=80, y=230)
	
	entry_5 = Entry(rootr, textvar=Aadhar)
	entry_5.place(x=240, y=230)

	label_6 = Label(rootr, text="AGE", width=20, font=("bold", 9))
	label_6.place(x=80, y=255)
		
	entry_6 = Entry(rootr, textvar=Age)
	entry_6.place(x=240, y=255)
	
	label_7 = Label(rootr, text="SALARY", width=20, font=("bold", 9))
	label_7.place(x=80, y=280)
	
	entry_7 = Entry(rootr, textvar=Salary)
	entry_7.place(x=240, y=280)	


	label_8 = Label(rootr, text="SELECT GENDER", width=20, font=("bold", 9))
	label_8.place(x=80, y=305)

	r1 = Radiobutton(rootr, text="MALE", padx=5, variable=var, value=1)
	r1.place(x=235, y=305)
	r2 = Radiobutton(rootr, text="FEMALE", padx=20, variable=var, value=2)
	r2.place(x=300, y=305)

	label_9 = Label(rootr, text="SELECT EMPLOYEE TYPE", width=20, font=("bold", 9))
	label_9.place(x=70, y=330)

	list12 = ['Doctor', 'Nurse', 'Floor sweeper'];

	droplist = OptionMenu(rootr, s, *list12)
	droplist.config(bg='yellow', fg='black', width=15)
	s.set('Select Employee Type')
	droplist.place(x=240, y=330)

	
	Button(rootr, text='Submit', width=20, bg='green', fg='black', command=edatabase).place(x=180, y=440)
	
	
	
	
	
	rootr.mainloop()


