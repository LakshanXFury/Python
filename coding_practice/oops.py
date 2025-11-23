"""
Design a class BankAccount with attributes account_number, balance, and methods deposit(), withdraw(), and get_balance()
Then subclass it into SavingsAccount that adds an interest_rate attribute and a method to apply interest.
"""


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Not enough Money, Remaining balance is :{self.balance}")

    def getbalance(self):
        return f"This is your current balance: {self.balance}"


# Using Inheritance / SubClass
class SavingsAccount(BankAccount):
    def __init__(self, interest_rate, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        decimal_value = self.interest_rate / 100
        interest = self.balance * decimal_value
        self.balance += interest
        return f"This is your balance post interest rate: {self.balance}"


person1 = SavingsAccount(account_number=523567, balance=4000, interest_rate=5)
person1.deposit(amount=100)
person1.withdraw(amount=500)
print(f"{person1.getbalance()} post withdrawal.")

# Apply interest on the updated balance
print(person1.apply_interest())