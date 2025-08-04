# cerinta 8.1
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        """Initialize a Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle (width * height)."""
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle (π * radius^2)."""
        import math

        return math.pi * (self.radius**2)


print(Rectangle.__doc__)
print(Circle.__doc__)

shapes = [Rectangle(4, 5), Circle(3), Rectangle(6, 7), Circle(5)]

rectangle_count = 0
circle_count = 0

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")
    if isinstance(shape, Rectangle):
        rectangle_count += 1
    elif isinstance(shape, Circle):
        circle_count += 1

print(f"Number of Rectangles: {rectangle_count}")
print(f"Number of Circles: {circle_count}")


# cerinta 8.2
class BankAccount:
    def __init__(self, balance=0):
        """Initialize bank account with a balance."""
        self._balance = balance

    @property
    def balance(self):
        """Get the current balance."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Set the balance, ensuring it's not negative."""
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account, ensuring enough balance."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount


account = BankAccount(100)

account.deposit(50)
print(f"Balance after deposit: {account.balance}")

account.withdraw(30)
print(f"Balance after withdrawal: {account.balance}")

try:
    account.deposit(-10)
except ValueError as e:
    print(f"Error: {e}")

try:
    account.withdraw(200)
except ValueError as e:
    print(f"Error: {e}")

try:
    account.balance = -50
except ValueError as e:
    print(f"Error: {e}")


# cerinta 8.3
class EmailNotification:
    def send(self, message):
        """Send an email notification."""
        print(f"Sending Email: {message}")


class SMSNotification:
    def send(self, message):
        """Send an SMS notification."""
        print(f"Sending SMS: {message}")


def send_bulk(notifiers, message):
    """Send a message using any list of notifiers."""
    for notifier in notifiers:
        notifier.send(message)


email_notifier = EmailNotification()
sms_notifier = SMSNotification()

send_bulk([email_notifier, sms_notifier], "Hello, this is a test message.")
