📚 Smart Campus Management System

A Python GUI application that integrates Student Management and a Banking System using SQLite database.
The application provides a user-friendly graphical interface built with Tkinter and stores data persistently using SQLite.

🚀 Features
🎓 Student Management

Add new student records

View all students

Store student details in database

Simple GUI input forms

💳 Banking System

Create bank account

Deposit money

Withdraw money

Maintain account balance

🖥 GUI Interface

User-friendly window interface

Buttons instead of command line

Popup messages for success/errors

🛠 Technologies Used
Technology	Purpose
Python	Core programming
Tkinter	GUI development
SQLite	Database storage
SQL	Data queries
📂 Project Structure
smart-campus-system
│
├── smart_campus_gui.py   # Main GUI application
├── campus.db             # SQLite database (auto created)
└── README.md             # Project documentation
⚙️ Installation
1️⃣ Install Python

Download and install Python from
https://www.python.org/

Check installation:

python --version
2️⃣ Clone or Download Project
git clone https://github.com/Ratheesh-DP/Smart-Campus-Management-System.git

Or download the ZIP file.

3️⃣ Run the Application
python smart_campus_gui.py
🗄 Database

The application automatically creates a database file:

campus.db

Tables created:

Students Table
Column	Type
roll	INTEGER
fname	TEXT
lname	TEXT
cgpa	REAL
dept	TEXT
Accounts Table
Column	Type
acc_no	INTEGER
name	TEXT
balance	REAL
📸 Application Interface

The GUI contains two main sections:

Student Management
Roll Number
First Name
Last Name
CGPA
Department
[Add Student] [View Students]
Banking System
Name
Initial Balance
[Create Account]

Account Number
Amount
[Deposit] [Withdraw]
🔮 Future Enhancements

Possible improvements:

Login authentication 🔐

Edit student details

Delete student records

Transaction history

Interest calculation

Better UI using PyQt

Export reports to Excel

🎯 Learning Outcomes

This project demonstrates:

Python programming

GUI development

Database integration

CRUD operations

Software modular design

👨‍💻 Author : Ratheesh-DP

Student Project – Smart Campus Management System

Developed for learning Python GUI and Database Programming.
