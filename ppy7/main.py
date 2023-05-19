import sqlite3
from tkinter import *

def create_table():
    mydb = sqlite3.connect('students.db')
    my_cursor = mydb.cursor()

    my_cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT,
                        last_name TEXT,
                        subject TEXT,
                        grade INTEGER
                    )''')

    mydb.commit()
    mydb.close()


def display_students():
    mydb = sqlite3.connect('students.db')
    my_cursor = mydb.cursor()

    my_cursor.execute("SELECT * FROM students")
    students = my_cursor.fetchall()

    students_listbox.delete(0, END)

    for student in students:
        students_listbox.insert(END, student)

    mydb.close()


def add_student():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    subject = subject_entry.get()
    grade = grade_entry.get()

    mydb = sqlite3.connect('students.db')
    my_cursor = mydb.cursor()

    my_cursor.execute("INSERT INTO students (first_name, last_name, subject, grade) VALUES (?, ?, ?, ?)",
                      (first_name, last_name, subject, grade))
    mydb.commit()

    mydb.close()

    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    subject_entry.delete(0, END)
    grade_entry.delete(0, END)


def delete_student():
    selected_student = students_listbox.get(students_listbox.curselection())

    student_id = selected_student[0]

    mydb = sqlite3.connect('students.db')
    my_cursor = mydb.cursor()

    my_cursor.execute("DELETE FROM students WHERE id=?",
                      (student_id,))
    mydb.commit()
    mydb.close()


def edit_student():
    selected_student = students_listbox.get(students_listbox.curselection())

    student_id = selected_student[0]

    new_first_name = edit_first_name_entry.get()
    new_last_name = edit_last_name_entry.get()
    new_subject = edit_subject_entry.get()
    new_grade = edit_grade_entry.get()

    mydb = sqlite3.connect('students.db')
    my_cursor = mydb.cursor()

    my_cursor.execute("UPDATE students SET first_name=?, last_name=?, subject=?, grade=? WHERE id=?",
                   (new_first_name, new_last_name, new_subject, new_grade, student_id))
    mydb.commit()
    mydb.close()

root = Tk()
root.title("Dane studentów")
root.geometry("500x800")
create_table()

students_label = Label(root, text="Studenci")
students_label.pack()

students_listbox = Listbox(root, width=60)
students_listbox.pack(pady=10)

display_button = Button(root, text="Wyświetl studentów", command=display_students)
display_button.pack(pady=5)

add_label = Label(root, text="Dodaj studenta")
add_label.pack()

first_name_label = Label(root, text="Imię:")
first_name_label.pack()
first_name_entry = Entry(root)
first_name_entry.pack()

last_name_label = Label(root, text="Nazwisko:")
last_name_label.pack()
last_name_entry = Entry(root)
last_name_entry.pack()

subject_label = Label(root, text="Przedmiot:")
subject_label.pack()
subject_entry = Entry(root)
subject_entry.pack()

grade_label = Label(root, text="Ocena:")
grade_label.pack()
grade_entry = Entry(root)
grade_entry.pack()

add_button = Button(root, text="Dodaj studenta", command=add_student)
add_button.pack(pady=10)

edit_label = Label(root, text="Edytuj studenta")
edit_label.pack()

edit_first_name_label = Label(root, text="Imię:")
edit_first_name_label.pack()
edit_first_name_entry = Entry(root)
edit_first_name_entry.pack()

edit_last_name_label = Label(root, text="Nazwisko:")
edit_last_name_label.pack()
edit_last_name_entry = Entry(root)
edit_last_name_entry.pack()

edit_subject_label = Label(root, text="Przedmiot:")
edit_subject_label.pack()
edit_subject_entry = Entry(root)
edit_subject_entry.pack()

edit_grade_label = Label(root, text="Ocena:")
edit_grade_label.pack()
edit_grade_entry = Entry(root)
edit_grade_entry.pack()

edit_button = Button(root, text="Edytuj studenta", command=edit_student)
edit_button.pack(pady=5)

delete_button = Button(root, text="Usuń studenta", command=delete_student)
delete_button.pack(pady=5)

root.mainloop()
