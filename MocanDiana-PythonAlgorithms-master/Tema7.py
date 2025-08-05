# 1. Shape area calculator with inheritance
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for geometric shapes. Requires an area() method."""
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    """Represents a rectangle. Calculates area as width * height."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle({self.width} x {self.height}), area: {self.area()}"

class Circle(Shape):
    """Represents a circle. Calculates area as pi * radius^2."""
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def __str__(self):
        return f"Circle(radius={self.radius}), area: {self.area():.2f}"

print(Rectangle.__doc__)
print(Circle.__doc__)

shapes = [Rectangle(3, 4), Circle(2), Rectangle(5, 6), Circle(1)]
rect_count = sum(isinstance(s, Rectangle) for s in shapes)
circ_count = sum(isinstance(s, Circle) for s in shapes)
for shape in shapes:
    print(shape)
print(f"Rectangles: {rect_count}, Circles: {circ_count}")

print("\n---\n")

# 2. Bank account with encapsulation
class BankAccount:
    """BankAccount with private balance, safe deposit/withdraw, and validation."""
    def __init__(self, initial=0):
        self._balance = initial
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount(100)
print("Initial balance:", account.balance)
account.deposit(50)
print("After deposit:", account.balance)
try:
    account.withdraw(200)
except ValueError as e:
    print("Withdraw error:", e)
try:
    account.balance = -10
except ValueError as e:
    print("Set balance error:", e)
try:
    account.deposit(-5)
except ValueError as e:
    print("Deposit error:", e)
account.withdraw(50)
print("After withdrawal:", account.balance)

print("\n---\n")

# 3. Notification system with polymorphism
class EmailNotification:
    """Sends notifications via email."""
    def send(self, message):
        print(f"[EMAIL] Notification: {message}")

class SMSNotification:
    """Sends notifications via SMS."""
    def send(self, message):
        print(f"[SMS] Notification: {message}")

def send_bulk(notifiers, message):
    for notifier in notifiers:
        notifier.send(message)

notifiers = [EmailNotification(), SMSNotification()]
send_bulk(notifiers, "System update at 5 PM.")