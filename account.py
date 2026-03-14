class Account:
    def __init__(self, acc_no, name, acc_type, balance, status="active"):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance
        self.status = status

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient balance")
        self.balance -= amount
