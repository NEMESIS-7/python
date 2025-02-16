class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    # def deposit(self, amount):
    #     self.balance += amount
    #     print(f"New balance: {self.balance}")

    def deposit(self, amount, note=None):
        self.balance += amount
        if note is not None:
            print(f"New balance: {self.balance}\nNote: {note}")
        else:
            print(f"New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount > 100:
            self.balance -= amount
            print(f"New balance: {self.balance}")
        else:
            raise Exception("Insufficient balance(you must have a minimum balance of 100) ")

    def display_account_details(self):
        print(f"Account holder name: {self.account_holder_name}, account number: {self.account_number}, balance: {self.balance}")
