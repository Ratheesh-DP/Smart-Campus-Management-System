from database.db_handler import DBHandler
from services.student_service import StudentService
from services.bank_service import BankService

def main():

    db = DBHandler()

    student_service = StudentService(db)
    bank_service = BankService(db)

    while True:

        print("\n====== SMART CAMPUS APP ======")
        print("1. Student Management")
        print("2. Banking System")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":

            print("\n--- Student Menu ---")
            print("1 Add Student")
            print("2 View Students")
            print("3 Delete Student")

            ch = input("Choice: ")

            if ch == "1":
                student_service.add_student()

            elif ch == "2":
                student_service.view_students()

            elif ch == "3":
                student_service.delete_student()

        elif choice == "2":

            print("\n--- Banking Menu ---")
            print("1 Create Account")
            print("2 Deposit")
            print("3 Withdraw")

            ch = input("Choice: ")

            if ch == "1":
                bank_service.create_account()

            elif ch == "2":
                bank_service.deposit()

            elif ch == "3":
                bank_service.withdraw()

        elif choice == "3":
            print("Thank you for using Smart Campus App")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
