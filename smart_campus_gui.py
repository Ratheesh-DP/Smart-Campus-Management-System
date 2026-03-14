import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------- DATABASE ----------
conn = sqlite3.connect("campus.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
roll INTEGER PRIMARY KEY,
fname TEXT,
lname TEXT,
cgpa REAL,
dept TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
balance REAL
)
""")

conn.commit()

# ---------- STUDENT FUNCTIONS ----------

def add_student():
    roll = roll_entry.get()
    fname = fname_entry.get()
    lname = lname_entry.get()
    cgpa = cgpa_entry.get()
    dept = dept_entry.get()

    cursor.execute("INSERT INTO students VALUES(?,?,?,?,?)",
                   (roll,fname,lname,cgpa,dept))
    conn.commit()

    messagebox.showinfo("Success","Student Added")

def view_students():

    window = tk.Toplevel(root)
    window.title("Student List")

    rows = cursor.execute("SELECT * FROM students").fetchall()

    for i,r in enumerate(rows):
        tk.Label(window,text=r).grid(row=i,column=0)


# ---------- BANK FUNCTIONS ----------

def create_account():

    name = acc_name_entry.get()
    balance = acc_balance_entry.get()

    cursor.execute("INSERT INTO accounts(name,balance) VALUES(?,?)",
                   (name,balance))

    conn.commit()

    messagebox.showinfo("Success","Account Created")

def deposit():

    acc = acc_no_entry.get()
    amount = dep_entry.get()

    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE acc_no=?",
                   (amount,acc))

    conn.commit()

    messagebox.showinfo("Success","Deposit Successful")

def withdraw():

    acc = acc_no_entry.get()
    amount = dep_entry.get()

    balance = cursor.execute("SELECT balance FROM accounts WHERE acc_no=?",
                             (acc,)).fetchone()

    if balance and float(amount) <= balance[0]:

        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE acc_no=?",
                       (amount,acc))

        conn.commit()

        messagebox.showinfo("Success","Withdrawal Successful")

    else:
        messagebox.showerror("Error","Insufficient Balance")

# ---------- GUI ----------

root = tk.Tk()
root.title("Smart Campus Management System")
root.geometry("500x500")

title = tk.Label(root,text="SMART CAMPUS APP",
                 font=("Arial",18,"bold"))
title.pack(pady=10)

# -------- STUDENT SECTION --------

frame1 = tk.LabelFrame(root,text="Student Management")
frame1.pack(pady=10)

tk.Label(frame1,text="Roll").grid(row=0,column=0)
roll_entry = tk.Entry(frame1)
roll_entry.grid(row=0,column=1)

tk.Label(frame1,text="First Name").grid(row=1,column=0)
fname_entry = tk.Entry(frame1)
fname_entry.grid(row=1,column=1)

tk.Label(frame1,text="Last Name").grid(row=2,column=0)
lname_entry = tk.Entry(frame1)
lname_entry.grid(row=2,column=1)

tk.Label(frame1,text="CGPA").grid(row=3,column=0)
cgpa_entry = tk.Entry(frame1)
cgpa_entry.grid(row=3,column=1)

tk.Label(frame1,text="Department").grid(row=4,column=0)
dept_entry = tk.Entry(frame1)
dept_entry.grid(row=4,column=1)

tk.Button(frame1,text="Add Student",command=add_student).grid(row=5,column=0)
tk.Button(frame1,text="View Students",command=view_students).grid(row=5,column=1)

# -------- BANK SECTION --------

frame2 = tk.LabelFrame(root,text="Banking System")
frame2.pack(pady=10)

tk.Label(frame2,text="Name").grid(row=0,column=0)
acc_name_entry = tk.Entry(frame2)
acc_name_entry.grid(row=0,column=1)

tk.Label(frame2,text="Initial Balance").grid(row=1,column=0)
acc_balance_entry = tk.Entry(frame2)
acc_balance_entry.grid(row=1,column=1)

tk.Button(frame2,text="Create Account",command=create_account).grid(row=2,column=0)

tk.Label(frame2,text="Account No").grid(row=3,column=0)
acc_no_entry = tk.Entry(frame2)
acc_no_entry.grid(row=3,column=1)

tk.Label(frame2,text="Amount").grid(row=4,column=0)
dep_entry = tk.Entry(frame2)
dep_entry.grid(row=4,column=1)

tk.Button(frame2,text="Deposit",command=deposit).grid(row=5,column=0)
tk.Button(frame2,text="Withdraw",command=withdraw).grid(row=5,column=1)

root.mainloop()
