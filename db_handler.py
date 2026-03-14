import sqlite3

class DBHandler:

    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            roll_no INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            cgpa REAL,
            quota TEXT,
            year INTEGER,
            department TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts(
            acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            type TEXT,
            balance REAL,
            status TEXT
        )
        """)

        self.conn.commit()
