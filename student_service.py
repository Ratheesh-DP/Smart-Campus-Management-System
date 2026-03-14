from models.student import Student

class StudentService:

    def __init__(self, db):
        self.db = db

    def add_student(self):

        roll = int(input("Roll No: "))
        fname = input("First Name: ")
        lname = input("Last Name: ")
        cgpa = float(input("CGPA: "))
        quota = input("Quota: ")
        year = int(input("Year: "))
        dept = input("Department: ")

        self.db.cursor.execute(
            "INSERT INTO students VALUES (?,?,?,?,?,?,?)",
            (roll, fname, lname, cgpa, quota, year, dept)
        )

        self.db.conn.commit()
        print("Student Added Successfully")

    def view_students(self):

        rows = self.db.cursor.execute("SELECT * FROM students").fetchall()

        for r in rows:
            print(r)

    def delete_student(self):

        roll = int(input("Enter roll number: "))
        self.db.cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
        self.db.conn.commit()

        print("Student Deleted")
