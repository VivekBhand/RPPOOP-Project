# RPPOOP-Project

## Topic - Hospital Management System

#### Vivek Bhand MIS : 111903129

#### Vipul Gaikwad MIS : 111903126

#### Vipin Ingle MIS : 111903125

# PREREQUISITES :
  ### PACKAGES
  
    1)Tkinter

    2)SQLITE3
 
  ## INSTALLATION 
   ```python
   pip install tk
   
   pip install pysqlite3
   ```
   ## Application to view .db files
    DB Browser for SQLite
    
   ## Import packages
   
   ```python
   from tkinter import *
   import sqlite3
   ```
   
   ## Operating System :
    Windows 10
    Ubuntu 20.04
   
   ## 
      


This hospital management project is made using the tkinter and sqlite in python

loginpage.py file contains the code for login page ( username and password is there in file itself)

menu.py contains the code of the menu which provides us choices

appointment.py file contains code for scheduling an appointment with doctor and also contains the code required for the database

covid.py this file contains the url for redirecting through the COVID DATA button

delete3.py contains the code for deleting the appointement 

# Database info


### Hospital management system

For our project of "Hospital Management System", to store store patients appointments and to store information of hospital employee, database system was required.
We chose "Structered Query Language"  SQLite for our need.

SQLite is a C library used in python that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.

To use SQLite3, sqlite3 is installed.



Import SQLite3 library:
```python
import sqlite3
```
## Patients Appointment
Open .db file: 
```
con = conn = sqlite3.connect('PATIENT APPOINTMENT RECORDS.db')

```
Create cursor object: 
```
with conn:
	cursor = conn.cursor()
```

Create .db file if not created: 
```
cursor.execute(
        'CREATE TABLE IF NOT EXISTS Patient (Fullname TEXT,Mobileno TEXT,Email TEXT,Aadhar TEXT,Age TEXT,Gender TEXT,Symptoms TEXT,Vaccine TEXT,Slot TEXT,City TEXT)')
```

Columns in .db file:
1. Fullname
2. Mobileno
3. Email
4. Aadhar
5. Age
6. Gender
7. Symptom
8. Vaccine
9. Slot
10. Slot

Insert in .db file :
```
cursor.execute('INSERT INTO Patient (FullName,Mobileno,Email,Aadhar,Age,Gender,Symptoms,Vaccine,Slot,City) VALUES(?,?,?,?,?,?,?,?,?,?)',
                   (name1, mobileno, email, aadhar ,age, gender,symptoms,vaccine, slot, city,))
 ```


## Employee Appointment
Open .db file: 
```
con = conn = sqlite3.connect('EMPLOYEE APPOINTMENT RECORDS.db')

```
Create cursor object: 
```
with conn:
	cursor = conn.cursor()
```

Create .db file if not created: 
```
cursor.execute(
        'CREATE TABLE IF NOT EXISTS Employee (Employeename TEXT,Employeeid TEXT,Mobileno TEXT,Email TEXT,Aadhar TEXT,Age TEXT,Salary TEXT,Gender TEXT,Employeetype TEXT)')
```

Columns in .db file:
1.Employeename
2.Employeeid
3.Mobileno
4.Email
5.Aadhar
6.Age
7.Salary
8.Var
9.Slot

Insert in .db file :
```
cursor.execute('INSERT INTO Employee (Employeename,Employeeid,Mobileno,Email,Aadhar,Age,Salary,Gender,Employeetype) VALUES(?,?,?,?,?,?,?,?,?)', 
                   (employeename, employeeid, mobile, email, aadhar, age, salary, gender, employeetype,))
 ```



