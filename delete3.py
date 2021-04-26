from tkinter import *
import sqlite3
from appointement import *
from os import system

root2 = None

#Aadhar = StringVar()
#Date = StringVar()


def deleteSqlRecord(aadhar):
    #aadhar = Aadhar.get()
    try:
        sqliteConnection = sqlite3.connect('PATIENT APPOINTMENT RECORDS.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_update_query = 'DELETE from Patient where Aadhar = ?'
        cursor.execute(sql_update_query, (aadhar,))
        sqliteConnection.commit()
        print("Record deleted successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


# deleteSqliteRecord(2)
def submitdel():
    delete = input("ENTER THE AADHAR NO:")
    deleteSqlRecord(delete)


def submit_search():
    # root2 = Tk()
    # root2.title("Search")
    print("ENTER ENTRIES IN DATABASE")
    aadhar = input("ENTER THE AADHAR NO:")
    search(aadhar)
    # delete_label = Label(root2, text='Aadhar no.', font=('calibre', 10, 'bold'))
    # delete_entry = Entry(root2, textvariable=Aadhar, font=('calibre', 10, 'normal'))
    # sub_btn = Button(root2, text='Submit', command=search)
    # delete_label.grid(row=0, column=0)
    # delete_entry.grid(row=0, column=1)
    # sub_btn.grid(row=2, column=1)

    # root2.mainloop()
def submit_searchd():
    print("ENTER ENTRIES IN DATABASE")
    date = input("ENTER THE DATE:")
    searchd(date)

def search(aadhar):
    # aadhar = Aadhar.get()
    try:
        conn = sqlite3.connect('PATIENT APPOINTMENT RECORDS.db')
        with conn:
            cursor = conn.cursor()
        print("Connected to SQLite")
        cursor.execute("SELECT * FROM Patient WHERE Aadhar=?", (aadhar,))

        rows = cursor.fetchall()
        conn.commit()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print("Failed to search record from a sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")
def searchd(date):
    # aadhar = Aadhar.get()
    try:
        conn = sqlite3.connect('PATIENT APPOINTMENT RECORDS.db')
        with conn:
            cursor = conn.cursor()
        print("Connected to SQLite")
        cursor.execute("SELECT * FROM Patient WHERE Date=?", (date,))

        rows = cursor.fetchall()
        conn.commit()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print("Failed to search record from a sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")