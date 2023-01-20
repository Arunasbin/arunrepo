from tkinter import*
from tkinter import ttk,Menu,Button
import sqlite3
conn=sqlite3.connect('Arun.db')
window=Tk()
window.title("FORM")
window.geometry("1000x1000")
window.config(bg="lightgreen")
conn.execute('''create table if not exists data(Name varchar(20),Address varchar(22),course varchar(20) ,Age int(20),EmailID varchar(32),genter varchar(20),MobileNo int(12));''')


def getdata():
    data1=entry_1.get()
    print(data1)
    data2=entry_2.get()
    print(data2)
    data3=entry_3.get()
    print(data3)
    data4=entry_4.get()
    print(data4)
    data5=entry_5.get()
    print(data5)
    data6=entry_6.get()
    print(data6)
    data7=entry_7.get()
    print(data7)
    conn.execute('''insert into data (Name,Address,course,Age,EmailID,genter,MobileNo)values(?,?,?,?,?,?,?)''',(data1,data2,data3,data4,data5,data6,data7))
    conn.commit()
def clear():
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)
    entry_5.delete(0,END)
    entry_6.delete(0,END)
    entry_7.delete(0,END)
    
   



menubar = Menu(window)  
file = Menu(menubar,tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
file.add_separator()  
file.add_command(label="Exit")  
menubar.add_cascade(label="File", menu=file)  

edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
menubar.add_cascade(label="Edit", menu=edit)  

help = Menu(menubar, tearoff=0)  
help.add_command(label="About")  
menubar.add_cascade(label="Help", menu=help)  
window.config(menu=menubar)

lab=Label(window,text="DETAILES",bg="green",fg="white",
          font=("times",20,"bold"),padx=30,pady=10)

lab.grid(row=0,column=0,padx=10,pady=10)
label_1 =Label(window,text="Name", width=20,font=("bold",10))
label_1.grid(row=1, column=0, padx=10, pady=10)
entry_1=Entry(window)
entry_1.grid(row=1, column=1, padx=10, pady=10)

lab.grid(row=0,column=0,padx=10,pady=10)
label_2 =Label(window,text="Address", width=20,font=("bold",10))
label_2.grid(row=2, column=0, padx=10, pady=10)
entry_2=Entry(window)
entry_2.grid(row=2, column=1, padx=10, pady=10)

lab.grid(row=0,column=0,padx=10,pady=10)
label_3 =Label(window,text="course", width=20,font=("bold",10))
label_3.grid(row=3, column=0, padx=10, pady=10)
entry_3=Entry(window)
entry_3.grid(row=3, column=1, padx=10, pady=10)


label_4=Label(window,text="Age", width=20,font=("bold",10))
label_4.grid(row=4, column=0, padx=10, pady=10)
entry_4=Entry(window)
entry_4.grid(row=4, column=1, padx=10, pady=10)


label_5=Label(window,text="Email ID", width=20,font=("bold",10))
label_5.grid(row=5, column=0, padx=10, pady=10)
entry_5=Entry(window)
entry_5.grid(row=5, column=1, padx=10, pady=10)

label_6=Label(window,text="genter", width=20,font=("bold",10))
label_6.grid(row=6, column=0, padx=10, pady=10)
entry_6=Entry(window)
entry_6.grid(row=6, column=1, padx=10, pady=10)


label_7=Label(window,text="Mobile No", width=20,font=("bold",10))
label_7.grid(row=7, column=0, padx=10, pady=10)
entry_7=Entry(window)
entry_7.grid(row=7, column=1, padx=10, pady=10)

b=Button(window, text='Submit' , width=20,bg="black",fg='white',cursor='hand2',command=getdata)
b.grid(row=8, column=1, columnspan=4, padx=10,pady=10)

b=Button(window, text='clear' , width=20,bg="red",fg='white',cursor='hand2',command=clear)
b.grid(row=8, column=3, columnspan=10, padx=10,pady=10)


window.mainloop()
