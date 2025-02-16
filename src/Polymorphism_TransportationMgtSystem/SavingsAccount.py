from BankAccount import BankAccount


class SavingsAccount(BankAccount):
    interest_rate = 0.0

    def __init__(self, account_holder_name, account_number, balance, interest_rate):
        BankAccount.__init__(self, account_holder_name, account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = (self.balance * 12 * self.interest_rate) / 100
        return f"Interest on {self.account_holder_name} : {interest:.2f}"

    def display_account_details(self):
        return (f"Account Details \n"
                f"Account holder: {self.account_holder_name}\n"
                f"Account balance: {self.balance:.2f}\n"
                f"Interest rate: {self.interest_rate}\n"
                f"Account number: {self.account_number}")



savingsAccount = SavingsAccount(
    "Alice",
    "SA123",
    500,
    0.03
)
print("\nAccount at creation")
print(savingsAccount.display_account_details())
#Depositing with note
savingsAccount.deposit(5000, "Acknowledge Me")
print("\nAccount after deposit")
print(savingsAccount.display_account_details())

#Trying to borrow past account balance
print("\n")
try:
    savingsAccount.withdraw(6000)
except Exception as e:
    print(str(e))

#Depositing without note
savingsAccount.deposit(5000)
print("\nAccount after Deposit")
print(savingsAccount.display_account_details())