from tkinter import *
import tkinter.messagebox 
import sqlite3

def func4():
    conn = sqlite3.connect('PATIENT APPOINTMENT RECORDS.db')
    c = conn.cursor()

    class Application:
            def __init__(self, master):
                self.master = master

                self.heading = Label(master, text="Update or Delete Appointments",  fg='steelblue', font=('arial 20'))
                self.heading.place(x=130, y=0)


                self.name = Label(master, text="Enter Patient's Name", font=('arial 13'))
                self.name.place(x=130, y=60)


                self.namenet = Entry(master, width=30)
                self.namenet.place(x=350, y=62)


                self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
                self.search.place(x=400, y=102)

            def search_db(self):
                self.input = self.namenet.get()


                sql = "SELECT * FROM Patient WHERE Fullname LIKE ?"
                self.res = c.execute(sql, (self.input,))
                for self.row in self.res:

                    if (self.row[0] == self.input ):
                        self.name = self.row[0]
                        self.mobile = self.row[1]
                        self.email = self.row[2]
                        self.aadhar  = self.row[3]
                        self.date = self.row[4]
                        self.age = self.row[5]
                        self.gender = self.row[6]
                        self.symptoms = self.row[7]
                        self.vaccine = self.row[8]
                        self.slot = self.row[9]
                        self.city = self.row[10]


                        self.uname = Label(self.master, text="Patient's Name", font=('arial 13'))
                        self.uname.place(  x=130, y=140)

                        self.umobile = Label(self.master, text="Mobile no.", font=('arial 13 '))
                        self.umobile.place(  x=130, y=180)

                        self.uemail = Label(self.master, text="Email", font=('arial 13  '))
                        self.uemail.place(  x=130, y=220)

                        self.uaadhar = Label(self.master, text="Aadhar", font=('arial 13  '))
                        self.uaadhar.place(  x=130, y=260)

                        self.udate = Label(self.master, text="Date", font=('arial 13  '))
                        self.udate.place(  x=130, y=300)

                        self.uage = Label(self.master, text="Age", font=('arial 13  '))
                        self.uage.place(  x=130, y=340)

                        self.ugender = Label(self.master, text="Gender", font=('arial 13  '))
                        self.ugender.place(  x=130, y=380)

                        self.usymptoms = Label(self.master, text="Symptoms", font=('arial 13  '))
                        self.usymptoms.place(  x=130, y=420)

                        self.uvaccine = Label(self.master, text="Vaccine", font=('arial 13  '))
                        self.uvaccine.place(  x=130, y=460)

                        self.uslot = Label(self.master, text="Slot", font=('arial 13  '))
                        self.uslot.place(  x=130, y=500)

                        self.ucity = Label(self.master, text="City", font=('arial 13  '))
                        self.ucity.place(  x=130, y=540)



                        self.ent1 = Entry(self.master, width=30)
                        self.ent1.place( x=300, y=140)
                        self.ent1.insert(END, str(self.name))

                        self.ent2 = Entry(self.master, width=30)
                        self.ent2.place( x=300, y=180)
                        self.ent2.insert(END, str(self.mobile))

                        self.ent3 = Entry(self.master, width=30)
                        self.ent3.place( x=300, y=220)
                        self.ent3.insert(END, str(self.email))

                        self.ent4 = Entry(self.master, width=30)
                        self.ent4.place( x=300, y=260)
                        self.ent4.insert(END, str(self.aadhar))

                        self.ent5 = Entry(self.master, width=30)
                        self.ent5.place( x=300, y=300)
                        self.ent5.insert(END, str(self.date))

                        self.ent6 = Entry(self.master, width=30)
                        self.ent6.place( x=300, y=340)
                        self.ent6.insert(END, str(self.age))

                        self.ent7 = Entry(self.master, width=30)
                        self.ent7.place( x=300, y=380)
                        self.ent7.insert(END, str(self.gender))

                        self.ent8 = Entry(self.master, width=30)
                        self.ent8.place( x=300, y=420)
                        self.ent8.insert(END, str(self.symptoms))

                        self.ent9 = Entry(self.master, width=30)
                        self.ent9.place( x=300, y=460)
                        self.ent9.insert(END, str(self.vaccine))

                        self.ent10 = Entry(self.master, width=30)
                        self.ent10.place( x=300, y=500)
                        self.ent10.insert(END, str(self.slot))

                        self.ent11 = Entry(self.master, width=30)
                        self.ent11.place( x=300, y=540)
                        self.ent11.insert(END, str(self.city))



                        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
                        self.update.place(x=400, y=580)


                        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
                        self.delete.place(x=130, y=580)
                    else:
                        tkinter.messagebox.showinfo("Error", "NOT FOUND")
            def update_db(self):

                self.var1 = self.ent1.get()
                self.var2 = self.ent2.get()
                self.var3 = self.ent3.get()
                self.var4 = self.ent4.get()
                self.var5 = self.ent5.get()
                self.var6 = self.ent6.get()
                self.var7 = self.ent7.get()
                self.var8 = self.ent8.get()
                self.var9 = self.ent9.get()
                self.var10 = self.ent10.get()
                self.var11 = self.ent11.get()


                query = "UPDATE Patient SET Fullname=?,Mobileno=?,Email=?,Aadhar=?,Date=?, Age=?, Gender=?,Symptoms=?,Vaccine=?,Slot=?, City=? WHERE Fullname LIKE ?"
                c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6,self.var7,self.var8,self.var9,self.var10,self.var11, self.namenet.get(),))
                conn.commit()
                tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
            def delete_db(self):

                sql2 = "DELETE FROM Patient WHERE Fullname LIKE ?"
                c.execute(sql2, (self.namenet.get(),))
                conn.commit()
                tkinter.messagebox.showinfo("Success", "Deleted Successfully")
                self.ent1.destroy()
                self.ent2.destroy()
                self.ent3.destroy()
                self.ent4.destroy()
                self.ent5.destroy()
                self.ent6.destroy()
                self.ent7.destroy()
                self.ent8.destroy()
                self.ent9.destroy()
                self.ent10.destroy()
                self.ent11.destroy()

    root = Tk()
    b = Application(root)
    root.geometry("600x800+600+0")
    root.mainloop()
