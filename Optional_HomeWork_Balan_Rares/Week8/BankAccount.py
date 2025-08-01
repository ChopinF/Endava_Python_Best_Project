class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = 0
        self.balance = initial_balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = value
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__balance}")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.__balance}")
account = BankAccount(100)
print(f"Initial balance: ${account.balance}")
account.deposit(50)
account.withdraw(30)
try:
    account.deposit(-20)
except ValueError as e:
    print("Error:", e)
try:
    account.withdraw(200)
except ValueError as e:
    print("Error:", e)
try:
    account.balance = -500
except ValueError as e:
    print("Error:", e)
print(f"Final balance: ${account.balance}")