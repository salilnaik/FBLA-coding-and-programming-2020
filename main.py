from tkinter import *
import csv
from tkinter import messagebox
from tkinter import ttk

current_index = 0
current_id = 0
current_student = ""
current_grade = 0
current_hour = 0
current_community = 0
current_service = 0
current_achievement = 0
student_info = []
sorted_rev = False
sorted_ = False


# Calls readInfo() and updates the list of students.
def updateList():
    list1.delete(0, len(student_info))
    if (len(student_info) > 0):
        for i in range(len(student_info)):
            list1.insert(i, student_info[i][0])
    else:
        list1.insert(0, "No students added yet")
    root.update()


# Reads data from the CSV file and adds it to the list student_info
def readInfo():
    global student_info
    with open("students.csv", "r", newline="") as students:
        student_info = []
        for row in csv.reader(students, delimiter=','):
            student_info.append(row)


# Writes data from student_info into the CSV file.
def writeInfo():
    global student_info
    with open("students.csv", "w", newline="") as students:
        csv.writer(students, delimiter=",").writerows(student_info)


# Updates the textbox displaying the selected student's information.
def updateMessage():
    global fff
    global root
    if len(student_info) > 0:
        fff.config(text="ID: " + str(current_id) + "\nStudent name: " +
                   current_student + "\nGrade: " + str(current_grade) +
                   "\nHours: " + str(current_hour) + "\nAwards: " + awards())
    else:
        fff.config(text="")
    root.update()


# Adds student to student_info given parameters of the
# name, grade, and number of service hours of the student,
# then calls writeInfo().
def addStudent(name, grade, hours, student_id):
    global student_info
    if (int(hours) >= 500):
        student_info.append([name, grade, hours, 1, 1, 1, student_id])
    elif (int(hours) >= 200):
        student_info.append([name, grade, hours, 1, 1, 0, student_id])
    elif (int(hours) >= 50):
        student_info.append([name, grade, hours, 1, 0, 0, student_id])
    else:
        student_info.append([name, grade, hours, 0, 0, 0, student_id])

    writeInfo()
    updateList()
    sort(0)


# Adds a student to student_info at a specific index, i
def addIndex(name, grade, hours, i, id_):
    global student_info
    global fff
    if (int(hours) >= 500):
        student_info.insert(i, [name, grade, hours, 1, 1, 1, id_])
    elif (int(hours) >= 200):
        student_info.insert(i, [name, grade, hours, 1, 1, 0, id_])
    elif (int(hours) >= 50):
        student_info.insert(i, [name, grade, hours, 1, 0, 0, id_])
    else:
        student_info.insert(i, [name, grade, hours, 0, 0, 0, id_])
    writeInfo()
    sort(0)
    fff.config(text="")


# Defines actions taken when the user selects a different student
# Updates the textbox displaying the selected student's information
def onSelect(evt):
    global student_info
    global current_index
    global current_id
    global current_student
    global current_grade
    global current_hour
    global current_community
    global current_service
    global current_achievement
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    if len(student_info) > 0:
        current_index = index
        current_student = value
        current_grade = student_info[index][1]
        current_hour = student_info[index][2]
        current_community = student_info[index][3]
        current_service = student_info[index][4]
        current_achievement = student_info[index][5]
        current_id = student_info[index][6]
        updateMessage()


# Opens a new window to add a student
def addWindow():
    global var1
    global var2
    global var3
    global var5
    global add
    global entryid
    global id_enable
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var5 = StringVar()
    add = Toplevel(root)
    add.title("Community Service Tracker ~ Add Student")
    add.configure(bg="#464646")
    Label(
        add,
        text="Please enter the information for the new student.",
        bg="#464646",
        fg="#fefefe").grid(
            row=0, column=0, columnspan=2)
    Label(
        add, text="Name", bg="#464646", fg="#fefefe").grid(
            row=1, column=0, padx=5, pady=5)
    Entry(
        add,
        bg="#464646",
        fg="#fefefe",
        relief='solid',
        highlightbackground="#fefefe",
        textvariable=var1).grid(
            row=1, column=1, padx=5, pady=5)
    Label(
        add, text="Grade", bg="#464646", fg="#fefefe").grid(
            row=2, column=0, padx=5, pady=5)
    Spinbox(
        add,
        bg="#464646",
        fg="#fefefe",
        buttonbackground="#464646",
        relief="solid",
        textvariable=var2,
        from_=1,
        to=12).grid(
            row=2, column=1, padx=5, pady=5)
    Label(
        add, text="Service Hours", bg="#464646", fg="#fefefe").grid(
            row=3, column=0, padx=5, pady=5)
    Spinbox(
        add,
        bg="#464646",
        fg="#fefefe",
        buttonbackground="#464646",
        relief="solid",
        textvariable=var3,
        from_=0,
        to=99999).grid(
            row=3, column=1, padx=5, pady=5)
    Label(
        add, text="Student ID", bg="#464646", fg="#fefefe").grid(
            row=4, column=0, padx=5, pady=5)
    entryid = Spinbox(
        add,
        bg="#464646",
        fg="#fefefe",
        buttonbackground="#464646",
        disabledbackground="#575757",
        relief="solid",
        textvariable=var5,
        from_=1,
        to=9999999999999999999999999)
    entryid.grid(row=4, column=1, padx=5, pady=5)
    id_enable = True
    assign()
    var4 = IntVar()
    var4.set(1)
    Checkbutton(
        add,
        text="Automatically assign student ID",
        variable=var4,
        bg="#464646",
        selectcolor="#464646",
        fg='#fefefe',
        relief="flat",
        command=assign).grid(
            row=5, column=1, padx=3, pady=5)
    Button(add, text="Submit", command=f).grid(row=6, column=1, padx=5, pady=5)
    add.update()
    add.mainloop()


def assign():
    global entryid
    global id_enable
    if id_enable:
        entryid.config(state="disabled")
        id_enable = False
    else:
        entryid.config(state="normal")
        id_enable = True


def nextId():
    global student_info
    id_list = []
    for u in student_info:
        id_list.append(int(u[6]))
    if (len(student_info) > 0):
        return int(max(id_list)) + 1
    return 1


# Getting the information from the textboxes
def f():
    global add
    id_list = []
    for u in student_info:
        id_list.append(u[6])
    if (var1.get().strip() != "" and (int(var2.get()) > 0
                                      and int(var2.get()) <= 12)
            and int(var3.get()) >= 0):
        if (id_enable):
            try:
                id_list.index(var5.get())
                messagebox.showinfo(
                    "Alert",
                    "That ID number is already in use, please choose a different one"
                )

            except ValueError:
                addStudent(var1.get(), var2.get(), var3.get(), var5.get())
                add.destroy()
                fff.config(text="")
        else:
            addStudent(var1.get(), var2.get(), var3.get(), nextId())
            add.destroy()
            fff.config(text="")

    else:
        messagebox.showinfo(
            "Alert",
            "Please enter a value for the name, grade, and service hours")


# Removing the selected student
def removeStudent():
    global list1
    global current_student
    global current_grade
    global current_hour
    try:
        index = int(list1.curselection()[0])
        value = list1.get(index)
        if (len(student_info) > 0):
            if messagebox.askyesno(
                    "Remove?", "Are you sure you want to remove the student " +
                    value + "?"):
                student_info.pop(index)
                writeInfo()
                updateList()
                updateMessage()
                sort(0)
                fff.config(text="")
        else:
            raise Exception()
    except:
        messagebox.showinfo("Alert", "Please select a student to remove")


# Calculates the awards earned by each student
def awards():
    global current_community
    global current_service
    global current_achievement

    if (current_achievement == "1"):
        return "Community, Service, Achievement"
    elif (current_service == "1"):
        return "Community, Service"
    elif (current_community == "1"):
        return "Community"
    else:
        return "None"


def select(index):
    global list1
    list1.select_clear(0, "end")
    list1.selection_set(index)
    list1.see(index)
    list1.activate(index)
    list1.selection_anchor(index)


# Gets the information from the textboxes
def editF():
    global edit
    global edit1
    global edit2
    global edit3
    global list1
    global fff
    global student_info
    global current_student
    global current_grade
    global current_hour
    global current_id
    index = current_index
    if (edit1.get().strip() != ""
            and (int(edit2.get()) > 0 and int(edit2.get()) <= 12)
            and int(edit3.get()) >= 0):
        student_info.pop(index)
        addIndex(edit1.get(), edit2.get(), edit3.get(), index, current_id)
        writeInfo()
        edit.destroy()
        updateList()
        sort(0)
        current_student = edit1.get()
        current_grade = edit2.get()
        current_hour = edit3.get()
    else:
        messagebox.showinfo(
            "Alert",
            "Please enter a value for the name, grade, and service hours")


# Closes the edit window
def editCancel():
    global edit
    edit.destroy()


# Opens the window to edit the student's information
def editWindow():
    global current_student
    global current_grade
    global current_hour
    global edit
    global edit1
    global edit2
    global edit3

    try:
        if (len(student_info) > 0):
            index = int(list1.curselection()[0])
            edit = Toplevel(root)
            edit.title("Community Service Tracker ~ Edit Student")
            edit.configure(bg="#464646")

            edit1 = StringVar()
            edit2 = StringVar()
            edit3 = StringVar()
            edit1.set(current_student)
            edit2.set(int(current_grade))
            edit3.set(int(current_hour))
            edit.configure(bg="#464646")
            Label(
                edit,
                text="Please edit the information for the student.",
                bg="#464646",
                fg="#fefefe").grid(
                    row=0, column=0, columnspan=2)
            Label(
                edit, text="Name", bg="#464646", fg="#fefefe").grid(
                    row=1, column=0, padx=5, pady=5)
            Entry(
                edit,
                bg="#464646",
                fg="#fefefe",
                relief='solid',
                highlightbackground="#fefefe",
                textvariable=edit1).grid(
                    row=1, column=1, padx=5, pady=5)
            Label(
                edit, text="Grade", bg="#464646", fg="#fefefe").grid(
                    row=2, column=0, padx=5, pady=5)
            Spinbox(
                edit,
                bg="#464646",
                fg="#fefefe",
                buttonbackground="#464646",
                relief="solid",
                textvariable=edit2,
                from_=1,
                to=12).grid(
                    row=2, column=1, padx=5, pady=5)
            Label(
                edit, text="Service Hours", bg="#464646", fg="#fefefe").grid(
                    row=3, column=0, padx=5, pady=5)
            Spinbox(
                edit,
                bg="#464646",
                fg="#fefefe",
                buttonbackground="#464646",
                relief="solid",
                textvariable=edit3,
                from_=0,
                to=99999).grid(
                    row=3, column=1, padx=5, pady=5)
            Button(
                edit,
                text="Submit",
                bg="#ababab",
                relief='flat',
                command=editF).grid(
                    row=4, column=1, padx=5, pady=5, sticky='W')
            Button(
                edit,
                text="Cancel",
                bg="#ababab",
                relief='flat',
                command=editCancel).grid(
                    row=4, column=1, padx=5, pady=5, sticky='E')

            edit.update()
            edit.mainloop()
        else:
            raise Exception
    except:
        messagebox.showinfo("Alert", "Please select a student to edit")


def hourF():
    global hour1
    global student_info
    global current_hour
    global hour

    index = current_index
    if (int(hour1.get()) > 0):
        name = student_info[index][0]
        grade = student_info[index][1]
        hours = student_info[index][2]
        id_ = student_info[index][6]
        student_info.pop(index)
        addIndex(name, grade, str(int(hours) + int(hour1.get())), index, id_)
        writeInfo()
        hour.destroy()
        updateList()
        current_student = name
        current_grade = grade
        current_hour = int(hours) + int(hour1.get())
        updateMessage()
        sort(0)
        select(current_index)

    else:
        messagebox.showinfo("Alert",
                            "Please enter a value for the service hours")


def hourWindow():
    global hour1
    global hour

    try:
        if (len(student_info) > 0):
            index = int(list1.curselection()[0])
            hour = Toplevel(root)
            hour.title("Community Service Tracker ~ Add Hours")
            hour.config(bg="#464646")

            hour1 = StringVar()
            Label(
                hour,
                bg="#464646",
                fg="#fefefe",
                text="Please enter the number of hours to add to the student."
            ).grid(
                row=0, column=0, padx=5, pady=5)
            Spinbox(
                hour,
                bg="#464646",
                fg="#fefefe",
                buttonbackground="#464646",
                relief="solid",
                textvariable=hour1,
                from_=0,
                to=99999).grid(
                    row=1, column=0, padx=5, pady=5)
            Button(
                hour,
                text="Submit",
                bg="#ababab",
                relief='flat',
                command=hourF).grid(
                    row=2, column=0, padx=5, pady=5)

            hour.update()
            hour.mainloop()
        else:
            raise Exception
    except:
        messagebox.showinfo("Alert", "Please select a student")


def sort(f):
    global student_info
    global sort_index
    global sort_options
    i = sort_options.index(sort_index.get())
    [x[0].lower() for x in student_info]
    try:
        student_info.sort(
            reverse=sorted_rev, key=lambda student_info: int(student_info[i]))
    except:
        student_info.sort(
            reverse=sorted_rev,
            key=lambda student_info: student_info[i].lower())
    updateList()


def flipSort():
    global sorted_rev
    global arrow_button
    if (sorted_rev):
        arrow_button.config(image=down_arrow)
        sorted_rev = False
        sort(0)
    else:
        arrow_button.config(image=up_arrow)
        sorted_rev = True
        sort(0)


root = Tk()
root.title("Community Service Tracker ~ Home")
root.configure(bg="#464646")
tab_parent = ttk.Notebook(root, style="TButton")

Label(root, text='Home', bg="#464646", fg="#fefefe").grid(row=0, column=0)

up_arrow = PhotoImage(file="up-arrow.png")
down_arrow = PhotoImage(file="down-arrow.png")

arrow_button = Button(root, image=down_arrow, relief="flat", command=flipSort)
arrow_button.grid(row=0, column=2, pady=5, padx=5, sticky='W')

sort_index = StringVar()
sort_options = [
    "Name", "Grade", "Hours", "Community Award", "Service Award",
    "Achievement Award", "ID"
]
popupMenu = ttk.OptionMenu(
    root, sort_index, "Name", *sort_options, command=sort)
popupMenu.grid(row=0, column=1, padx=5, pady=5, sticky='E')

Button(
    root, text="Add Student", bg="#74d9f2", relief="flat",
    command=addWindow).grid(
        row=1, column=1, columnspan=2)
Button(
    root, text="Edit Student", bg="#ababab", relief="flat",
    command=editWindow).grid(
        row=2, column=1, columnspan=2)
Button(
    root,
    text="Remove Student",
    bg="#ff4d4d",
    relief="flat",
    command=removeStudent).grid(
        row=3, column=1, padx=5, columnspan=2)
Button(
    root, text="Add Hours", bg="#ababab", relief="flat",
    command=hourWindow).grid(
        row=4, column=1, columnspan=2)

list1 = Listbox(
    root,
    selectmode='SINGLE',
    bg="#464646",
    relief="flat",
    fg="#fefefe",
    selectbackground="#ababab",
    name="list1",
    width=40)

list1.bind('<<ListboxSelect>>', onSelect)

readInfo()
updateList()
sort(0)
list1.grid(row=1, padx=5, pady=5, rowspan=5)

fff = Message(root, text="", bg="#464646", fg="#fefefe", width=250)
fff.grid(row=6, column=0, sticky='W')

root.update()
root.mainloop()
