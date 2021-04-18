from tkinter import *
import sqlite3
from registration import *
#root2=None

delete_var = StringVar()

def deleteSqliteRecord(Aadhar):
    try:
        sqliteConnection = sqlite3.connect('PATIENT APPOINTMENT RECORDS.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """DELETE from Patient where Aadhar = ?"""
        cursor.execute(sql_update_query, (Aadhar,))
        sqliteConnection.commit()
        print("Record deleted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete reocord from a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

#deleteSqliteRecord(2)
def submit():
    root2 = Tk()
    root2.title("Delete")

    
    delete=delete_var.get()
    
    print(delete)
    delete_label = Label(root2, text = 'Aadhar no.', font=('calibre',10, 'bold'))
    delete_entry = Entry(root2,textvariable = delete_var, font=('calibre',10,'normal'))
    sub_btn= Button(root2,text = 'Submit', command = deleteSqliteRecord(delete))
    delete_label.grid(row=0,column=0)
    delete_entry.grid(row=0,column=1)
    sub_btn.grid(row=2,column=1)
    
    root2.mainloop()
    











