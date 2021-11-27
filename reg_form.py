from tkinter import *
import sqlite3

root=Tk()
root.configure(background='green')
root.title("Registration form")
root.geometry("500x200")

Fu=StringVar()
co=StringVar()
se =StringVar()
fnum =StringVar()
pnum=StringVar()
ema=StringVar()
adr=StringVar()

def database():
    Fname=Fu.get()
    cours=co.get()
    semester=se.get()
    form=fnum.get()
    contact=pnum.get()
    mail=ema.get()
    addr=adr.get()
    

    conn = sqlite3.connect('Form.db')
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data (Fullname TEXT,Course TEXT,Semester TEXT,FormNumber TEXT,Contact TEXT,EMail TEXT,Address TEXT)')
    cursor.execute('INSERT INTO data (FullName,Course,Semester,FormNumber,Contact,EMail,Address) VALUES(?,?,?,?,?,?,?)',
                  (Fname,cours,semester,form,contact,mail,addr,))
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('Form.db')
    cursor=conn.cursor()
    cursor.execute("DELETE FROM data WHERE FormNumber="+form_no_field.get())
    conn.commit()
    conn.close()

    
def Search():
    conn = sqlite3.connect("Form.db")
    cursor = conn.execute("Select * from data where FormNumber = '"+str(fnum.get())+"'")
    for row in cursor:
        Fu.set(row[0])
        co.set(row[1])
        se.set(row[2])
        fnum.set(row[3])
        pnum.set(row[4])
        ema.set(row[5])
        adr.set(row[6])
    conn.commit()
    conn.close()
    
def Update():
    conn = sqlite3.connect("Form.db")
    conn.execute("Update data set Course = '"+str(co.get())+"' where FormNumber = '"+str(fnum.get())+"'")
    conn.execute("Update data set Semester = '"+str(se.get())+"' where FormNumber = '"+str(fnum.get())+"'")
    conn.execute("Update data set Fullname = '"+str(Fu.get())+"' where FormNumber = '"+str(fnum.get())+"'")
    conn.execute("Update data set Contact = '"+str(pnum.get())+"' where FormNumber = '"+str(fnum.get())+"'")
    conn.execute("Update data set Email = '"+str(ema.get())+"' where FormNumber = '"+str(fnum.get())+"'")
    conn.execute("Update data set Address = '"+str(adr.get())+"' where FormNumber = '"+str(fnum.get())+"'")
    conn.commit()
    conn.close()
    
    
heading = Label(root, text="Form", bg="green")
name = Label(root, text="Name", bg="green")
course = Label(root, text="Course", bg="green")
sem = Label(root, text="Semester", bg="green")
form_no = Label(root, text="Form No.", bg="green")
contact_no = Label(root, text="Contact No.", bg="green")
email_id = Label(root, text="Email id", bg="green")
address = Label(root, text="Address", bg="green")

heading.grid(row=0, column=1) 
name.grid(row=1, column=0) 
course.grid(row=2, column=0) 
sem.grid(row=3, column=0) 
form_no.grid(row=4, column=0) 
contact_no.grid(row=5, column=0) 
email_id.grid(row=6, column=0) 
address.grid(row=7, column=0) 

name_field = Entry(root,textvar=Fu) 
course_field = Entry(root,textvar=co) 
sem_field = Entry(root,textvar=se) 
form_no_field = Entry(root,textvar=fnum) 
contact_no_field = Entry(root,textvar=pnum) 
email_id_field = Entry(root,textvar=ema) 
address_field = Entry(root,textvar=adr) 

name_field.grid(row=1, column=1, ipadx="100") 
course_field.grid(row=2, column=1, ipadx="100") 
sem_field.grid(row=3, column=1, ipadx="100") 
form_no_field.grid(row=4, column=1, ipadx="100") 
contact_no_field.grid(row=5, column=1, ipadx="100") 
email_id_field.grid(row=6, column=1, ipadx="100") 
address_field.grid(row=7, column=1, ipadx="100")

submit = Button(root, text="Submit", fg="Black", bg="Red",command=database)
submit.place(x=95,y=170)
delete_data=Button(root,text="Delete",fg="Black",bg="Red",command=delete)
delete_data.place(x=170,y=170)
search_button=Button(root,text="search",fg="Black",bg="Red",command=Search)
search_button.place(x=245,y=170)
update_button=Button(root,text="update",fg="Black",bg="Red",command=Update)
update_button.place(x=320,y=170)
root.mainloop()