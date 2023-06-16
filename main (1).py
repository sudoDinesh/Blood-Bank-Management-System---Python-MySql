from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
import random
db = Database('PLASMABANK','root','12345678')

# notebook  
root5 = Tk()
root5.title("Blood Bank Management System")
root5.geometry("1920x1080+0+0")
root5.config(bg="#2c3e50")
root5.state("zoomed")
tabControl = ttk.Notebook(root5)


root = ttk.Frame(tabControl)
root1 = ttk.Frame(tabControl)
#root2 = ttk.Frame(tabControl)
#root3 = ttk.Frame(tabControl)


tabControl.add(root, text ='Donor')
tabControl.add(root1, text ='Staff')
#tabControl.add(root2, text ='Tab 3')
#tabControl.add(root3, text ='Tab 4')

tabControl.pack(expand = 1, fill ="both")

donorID = StringVar()
name = StringVar()
bType = StringVar()
dob = StringVar()
age = StringVar()
gender = StringVar()
address = StringVar()
contact = StringVar()
date = StringVar()
companion = StringVar()
relation = StringVar()


# Entries Frame1
entries_frame = Frame(root, bg="#9A9AFF")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="DONOR INFO", font=("Calibri", 18, "bold"), bg="#9A9AFF", fg="black")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")


#row 1

r1_frame = Frame(entries_frame, bg="#9A9AFF")
r1_frame.grid(row=1, column=0, columnspan=10, padx=10, pady=10, sticky="w")



lblDonor = Label(r1_frame, text="name", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblDonor.grid(row=0, column=0, padx=10, pady=10, sticky="w")
txtDonor = Entry(r1_frame, textvariable=name, font=("Calibri", 16), width=20)
txtDonor.grid(row=0, column=1, padx=10, pady=10, sticky="w")

lblName = Label(r1_frame, text="name", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblName.grid(row=0, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(r1_frame, textvariable=name, font=("Calibri", 16), width=20)
txtName.grid(row=0, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(r1_frame, text="Age", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblAge.grid(row=0, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(r1_frame, textvariable=age, font=("Calibri", 16), width=10)
txtAge.grid(row=0, column=3, padx=10, pady=10, sticky="w")

lbldob = Label(r1_frame, text="dob", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lbldob.grid(row=0, column=4, padx=10, pady=10, sticky="w")
txtdob = Entry(r1_frame, textvariable=dob, font=("Calibri", 16), width=15)
txtdob.grid(row=0, column=5, padx=10, pady=10, sticky="w")

lblBtype = Label(r1_frame, text="Blood Type", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblBtype.grid(row=0, column=6, padx=10, pady=10, sticky="w")
txtBtype = Entry(r1_frame, textvariable=bType, font=("Calibri", 16), width=10)
txtBtype.grid(row=0, column=7, padx=10, pady=10, sticky="w")

lblGender = Label(r1_frame, text="gender", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblGender.grid(row=0, column=8, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(r1_frame, font=("Calibri", 16), width=15, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=0, column=9, padx=10, sticky="w")



#row 2

r2_frame = Frame(entries_frame, bg="#9A9AFF")
r2_frame.grid(row=2, column=0, columnspan=8, padx=10, pady=10, sticky="w")

lblContact = Label(r2_frame, text="Contact No", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblContact.grid(row=0, column=0, padx=10, pady=10, sticky="w")
txtContact = Entry(r2_frame, textvariable=contact, font=("Calibri", 16), width=20)
txtContact.grid(row=0, column=1, padx=10, sticky="w")

lblDate = Label(r2_frame, text="Date", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblDate.grid(row=0, column=2, padx=10, pady=10, sticky="w")
txtDate = Entry(r2_frame, textvariable=date, font=("Calibri", 16), width=15)
txtDate.grid(row=0, column=3, padx=10, sticky="w")

lblCompanion = Label(r2_frame, text="Companion", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblCompanion.grid(row=0, column=4, padx=10, pady=10, sticky="w")
txtCompanion = Entry(r2_frame, textvariable=companion, font=("Calibri", 16), width=20)
txtCompanion.grid(row=0, column=5, padx=10, sticky="w")

lblRelation = Label(r2_frame, text="Relation", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblRelation.grid(row=0, column=6, padx=10, pady=10, sticky="w")
txtRelation = Entry(r2_frame, textvariable=relation, font=("Calibri", 16), width=20)
txtRelation.grid(row=0, column=7, padx=10, sticky="w")



#row 3

lblDonorID = Label(entries_frame, text="DonorID", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblDonorID.grid(row=3, column=1, padx=10, pady=10, sticky="w")


lblAddress = Label(entries_frame, text= "Address", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblAddress.grid(row=3, column=0, padx=10, pady=10, sticky="w")


#row 4


txtDonorID = Entry(entries_frame,font=("Calibri", 16), textvariable=donorID, width=20, state = DISABLED)
txtDonorID.grid(row=4, column=1, padx=10, sticky="w")

txtAddress = Entry(entries_frame, textvariable=address,font=("Calibri", 16), width=85)
txtAddress.grid(row=4, column=0, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    donorID.set(row[0])
    name.set(row[1])
    bType.set(row[2])
    contact.set(row[3])
    dob.set(row[4])
    age.set(row[5])
    gender.set(row[6])
    address.set(row[7])
    date.set(row[8])
    companion.set(row[9])
    relation.set(row[10])


def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txtName.get() == "" or txtBtype.get() == "" or txtContact.get() == "" or txtdob.get() == "" or txtAge.get() == "" or comboGender.get() == "" or txtAddress.get() == "" or txtDate.get() == '' or txtCompanion.get() == '' or txtRelation.get() == '':
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    d = txtdob.get()
    if(not(len(d) == 10 and d[2] == '-' and d[5] == '-' and d[-5] == '-' and d[:2].isdigit() and d[3:5].isdigit() and d[-4:].isdigit() and int(d[:2]) < 32 and int(d[:2]) > 0 and int(d[3:5]) > 0 and int(d[3:5]) <13)):
        messagebox.showerror("Erorr in Input","Invalid date of birth")
        return
    d = txtDate.get()
    if(not(len(d) == 10 and d[2] == '-' and d[5] == '-' and d[-5] == '-' and d[:2].isdigit() and d[3:5].isdigit() and d[-4:].isdigit() and int(d[:2]) < 32 and int(d[:2]) > 0 and int(d[3:5]) > 0 and int(d[3:5]) <13)):
        messagebox.showerror("Erorr in Input","Invalid date of ")
        return
    elif(not(len(p) == 10 and p.isdigit())):
        messagebox.showerror("Erorr in Input","Invalid contact number")
        return
    elif(int(age.get()) < 0 or int(age.get()) > 110):
        messagebox.showerror("Erorr in Input","Invalid age")
        return
    elif(bType.get() not in ['A+ve','A-ve','AB+ve','AB-ve',"O+ve","O-ve","RH","Bombay blood","B+ve"]):
        messagebox.showerror("Erorr in Input","Invalid Blood type")
        return
    ddonorId = random.randrange(100,100000)
    DonorID=("DN"+str(ddonorId))
    donorID.set(DonorID)
    db.insert(DonorID,name.get(),bType.get(),dob.get(),age.get(),gender.get(),address.get(),contact.get(),date.get(),companion.get(),relation.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()

def update_employee():
    if txtName.get() == "" or txtBtype.get() == "" or txtContact.get() == "" or txtdob.get() == "" or txtAge.get() == "" or comboGender.get() == "" or txtAddress.get() == "" or txtDate.get() == '' or txtCompanion.get() == '' or txtRelation.get() == '':
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    d = txtdob.get()
    if(not(len(d) == 10 and d[2] == '-' and d[5] == '-' and d[-5] == '-' and d[:2].isdigit() and d[3:5].isdigit() and d[-4:].isdigit() and int(d[:2]) < 32 and int(d[:2]) > 0 and int(d[3:5]) > 0 and int(d[3:5]) <13)):
        messagebox.showerror("Erorr in Input","Invalid date of birth")
        return
    d = txtDate.get()
    if(not(len(d) == 10 and d[2] == '-' and d[5] == '-' and d[-5] == '-' and d[:2].isdigit() and d[3:5].isdigit() and d[-4:].isdigit() and int(d[:2]) < 32 and int(d[:2]) > 0 and int(d[3:5]) > 0 and int(d[3:5]) <13)):
        messagebox.showerror("Erorr in Input","Invalid date of donation")
        return
    p = contact.get()
    if(not(len(p) == 10 and p.isdigit())):
        messagebox.showerror("Erorr in Input","Invalid contact number")
        return
    elif(int(age.get()) < 0 or int(age.get()) > 110):
        messagebox.showerror("Erorr in Input","Invalid age")
        return
    elif(bType.get() not in ['A+ve','A-ve','AB+ve','AB-ve',"O+ve","O-ve","RH","Bombay blood","B+ve"]):
        messagebox.showerror("Erorr in Input","Invalid Blood type")
        return
    db.update(donorID.get(),name.get(),bType.get(),dob.get(),age.get(),gender.get(),address.get(),contact.get(),date.get(),companion.get(),relation.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(donorID.get())
    clearAll()
    dispalyAll()
    messagebox.showinfo("Success", "Record Deleted")

def clearAll():
    name.set("")
    bType.set("")
    dob.set("")
    age.set("")
    gender.set("")
    address.set("")
    contact.set("")
    date.set("")
    companion.set("")
    relation.set("")
    donorID.set("")


btn_frame = Frame(entries_frame, bg="#9A9AFF")
btn_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="red",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="green", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="orange", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="brown",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame

tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=325, width=1980, height=520)
scroll_x=Scrollbar(tree_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(tree_frame,orient=VERTICAL)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 14),rowheight=50)

# Modify the font of the body

style.configure("mystyle.Treeview.Heading", font=('Calibri', 14))


# Modify the font of the headings


tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), style="mystyle.Treeview",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)


tv.heading("1", text="ID")
tv.column("1", width=120,stretch = NO)
tv.heading("2", text="Name")
tv.column("2",width=150,stretch = NO)
tv.heading("3", text="Blood Type")
tv.column("3", width=100,stretch = NO)
tv.heading("4", text="Contact")
tv.column("4",width=150,stretch = NO)
tv.heading("5", text="DOB")
tv.column("5", width=100,stretch = NO)
tv.heading("6", text="Age")
tv.column("6",width=80,stretch = NO)
tv.heading("7", text="Gender")
tv.column("7",width=100,stretch = NO)
tv.heading("8",text="Address")
tv.column("8",width=200,stretch = NO)
tv.heading("9",text="date")
tv.column("9",width=100,stretch = NO)
tv.heading("10",text="companion")
tv.column("10",width=150,stretch = NO)
tv.heading("11",text="relation")
tv.column("11",width=150,stretch = NO)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()





#**********************************************************************************************************************************************


#table 2

Eid = StringVar()
Ename = StringVar()
dob1 = StringVar()
contact1= StringVar()
gender1 = StringVar()
sal = StringVar()
address1 = StringVar()



# Entries Frame1
entries_frame1 = Frame(root1, bg="#9A9AFF")
entries_frame1.pack(side=TOP, fill=X)
title1 = Label(entries_frame1, text="STAFF DETAILS", font=("Calibri", 18, "bold"), bg="#9A9AFF", fg="black")
title1.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")


#row 1

r11_frame = Frame(entries_frame1, bg="#9A9AFF")
r11_frame.grid(row=1, column=0, columnspan=8, padx=10, pady=10, sticky="w")



lblEmp = Label(r11_frame, text="Employee id", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblEmp.grid(row=0, column=0, padx=10, pady=10, sticky="w")
txtEmp = Entry(r11_frame, textvariable=Eid, font=("Calibri", 16), width=20,state=DISABLED)
txtEmp.grid(row=0, column=1, padx=10, pady=10, sticky="w")

lblEname = Label(r11_frame, text="Employee Name", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblEname.grid(row=0, column=2, padx=10, pady=10, sticky="w")
txtEname = Entry(r11_frame, textvariable=Ename, font=("Calibri", 16), width=20)
txtEname.grid(row=0, column=3, padx=10, pady=10, sticky="w")

lbldob1 = Label(r11_frame, text="dob", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lbldob1.grid(row=0, column=4, padx=10, pady=10, sticky="w")
txtdob1 = Entry(r11_frame, textvariable=dob1, font=("Calibri", 16), width=15)
txtdob1.grid(row=0, column=5, padx=10, pady=10, sticky="w")



#row 2

r22_frame = Frame(entries_frame1, bg="#9A9AFF")
r22_frame.grid(row=2, column=0, columnspan=8, padx=10, pady=10, sticky="w")

lblContact1 = Label(r22_frame, text="Contact No", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblContact1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
txtContact1 = Entry(r22_frame, textvariable=contact1, font=("Calibri", 16), width=20)
txtContact1.grid(row=0, column=1, padx=10, sticky="w")


lblGender1 = Label(r22_frame, text="Gender", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblGender1.grid(row=0, column=2, padx=10, pady=10, sticky="w")
comboGender1 = ttk.Combobox(r22_frame, font=("Calibri", 16), width=15, textvariable=gender1, state="readonly")
comboGender1['values'] = ("Male", "Female")
comboGender1.grid(row=0, column=3, padx=10, sticky="w")



lblSal = Label(r22_frame, text="Salary", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblSal.grid(row=0, column=4, padx=10, pady=10, sticky="w")
txtSal = Entry(r22_frame, textvariable=sal, font=("Calibri", 16), width=20)
txtSal.grid(row=0, column=5, padx=10, sticky="w")



#row 3
lblAddress1 = Label(entries_frame1, text="Address", font=("Calibri", 16), bg="#9A9AFF", fg="black")
lblAddress1.grid(row=3, column=0, padx=10, pady=10, sticky="w")


#row 4

txtAddress1 = Entry(entries_frame1, textvariable=address1,font=("Calibri", 16), width=85)
txtAddress1.grid(row=4, column=0, padx=10, sticky="w")



def getData(event):
    selected_row1 = tv1.focus()
    data1 = tv1.item(selected_row1)
    global row1
    row1 = data1["values"]
    Eid.set(row1[0])
    Ename.set(row1[1])
    dob1.set(row1[2])
    gender1.set(row1[3])
    contact1.set(row1[4])
    sal.set(row1[5])
    address1.set(row1[6])
    

def dispalyAll1():
    tv1.delete(*tv1.get_children())
    for row in db.fetch1():
        tv1.insert("", END,values=row)


def add_employee1():
    if Ename.get() == "" or contact1.get() == "" or dob1.get() == '' or gender1.get() == "" or sal.get() == "" or address1.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    d = dob1.get()
    if(not(len(d) == 10 and d[2] == '-' and d[5] == '-' and d[-5] == '-' and d[:2].isdigit() and d[3:5].isdigit() and d[-4:].isdigit() and int(d[:2]) < 32 and int(d[:2]) > 0 and int(d[3:5]) > 0 and int(d[3:5]) <13)):
            messagebox.showerror("Erorr in Input","Invalid date")
            return
    p = contact1.get()
    if(not(len(p) == 10 and p.isdigit())):
        messagebox.showerror("Erorr in Input","Invalid contact number")
        return
    p = sal.get()
    if(not(p.isdigit())):
        messagebox.showerror("Erorr in Input","Invalid salary")
        return
    EEid = random.randrange(100,100000)
    eid=("E"+str(EEid))
    Eid.set(eid)
    db.insert1(Eid.get(),Ename.get(),contact1.get(),dob1.get(),gender1.get(),sal.get(),address1.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll1()
    dispalyAll1()



def update_employee1():
    if Eid.get() == "" or Ename.get() == "" or contact1.get() == "" or gender1.get() == "" or dob1.get() == '' or sal.get() == "" or address1.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    d = dob1.get()
    if(not(len(d) == 10 and d[2] == '-' and d[5] == '-' and d[-5] == '-' and d[:2].isdigit() and d[3:5].isdigit() and d[-4:].isdigit() and int(d[:2]) < 32 and int(d[:2]) > 0 and int(d[3:5]) > 0 and int(d[3:5]) <13)):
        messagebox.showerror("Erorr in Input","Invalid date")
        return
    p = contact1.get()
    if(not(len(p) == 10 and p.isdigit())):
        messagebox.showerror("Erorr in Input","Invalid contact number")
        return
    p = sal.get()
    if(not(p.isdigit())):
        messagebox.showerror("Erorr in Input","Invalid salary")
        return
    db.update1(Eid.get(),Ename.get(),contact1.get(),dob1.get(),gender1.get(),sal.get(),address1.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll1()
    dispalyAll1()


def delete_employee1():
    db.remove1(Eid.get())
    messagebox.showinfo("Success", "Record Deleted")
    clearAll1()
    dispalyAll1()


def clearAll1():
    Eid.set('')
    Ename.set('')
    dob1.set('')
    contact1.set('')
    gender1.set('')
    address1.set('')
    sal.set('')

    
btn_frame1 = Frame(entries_frame1, bg="#9A9AFF")
btn_frame1.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd1 = Button(btn_frame1, command=add_employee1, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="red",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit1 = Button(btn_frame1, command=update_employee1, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="green", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete1 = Button(btn_frame1, command=delete_employee1, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="orange", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear1 = Button(btn_frame1, command=clearAll1, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="brown",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame

tree_frame1= Frame(root1, bg="#ecf0f1")
tree_frame1.place(x=0, y=325, width=1980, height=520)
scroll_x1=Scrollbar(tree_frame1,orient=HORIZONTAL)
scroll_y1=Scrollbar(tree_frame1,orient=VERTICAL)

style1 = ttk.Style()
style1.configure("mystyle.Treeview", font=('Calibri', 14),rowheight=50)

# Modify the font of the body

style1.configure("mystyle.Treeview.Heading", font=('Calibri', 14))


# Modify the font of the headings


tv1 = ttk.Treeview(tree_frame1, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview",xscrollcommand=scroll_x1.set,yscrollcommand=scroll_y1.set)
scroll_x1.pack(side=BOTTOM,fill=X)
scroll_y1.pack(side=RIGHT,fill=Y)


tv1.heading("1", text="Eid")
tv1.column("1", width=170,stretch = NO)
tv1.heading("2", text="Ename")
tv1.column("2",width=200,stretch = NO)
tv1.heading("3", text="DOB")
tv1.column("3", width=150,stretch = NO)
tv1.heading("4", text="Gender")
tv1.column("4",width=200,stretch = NO)
tv1.heading("5", text="Contact")
tv1.column("5", width=150,stretch = NO)
tv1.heading("6", text="Salary")
tv1.column("6",width=170,stretch = NO)
tv1.heading("7", text="Address")
tv1.column("7",width=400,stretch = NO)

tv1['show'] = 'headings'
tv1.bind("<ButtonRelease-1>", getData)
tv1.pack(fill=X)

dispalyAll1()
root.mainloop()

