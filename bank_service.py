class BankService:

    def __init__(self, db):
        self.db = db

    def create_account(self):

        name = input("Account Holder: ")
        acc_type = input("Type (savings/current): ")
        balance = float(input("Initial Balance: "))

        self.db.cursor.execute(
            "INSERT INTO accounts(name,type,balance,status) VALUES (?,?,?,?)",
            (name, acc_type, balance, "active")
        )

        self.db.conn.commit()

        print("Account Created")

    def deposit(self):

        acc = int(input("Account number: "))
        amount = float(input("Deposit amount: "))

        self.db.cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE acc_no=?",
            (amount, acc)
        )

        self.db.conn.commit()

        print("Deposit successful")

    def withdraw(self):

        acc = int(input("Account number: "))
        amount = float(input("Withdraw amount: "))

        balance = self.db.cursor.execute(
            "SELECT balance FROM accounts WHERE acc_no=?",
            (acc,)
        ).fetchone()[0]

        if amount > balance:
            print("Insufficient balance")
            return

        self.db.cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE acc_no=?",
            (amount, acc)
        )

        self.db.conn.commit()

        print("Withdrawal successful")
