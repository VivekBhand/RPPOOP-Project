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


