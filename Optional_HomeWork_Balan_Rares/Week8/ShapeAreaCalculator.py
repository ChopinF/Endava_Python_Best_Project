from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle ({self.width} x {self.height}) - Area: {self.area()}"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def __str__(self):
        return f"Circle (radius {self.radius}) - Area: {self.area():.2f}"
if __name__ == "__main__":
    print("Rectangle Docstring:")
    print(Rectangle.__doc__)
    print("\nCircle Docstring:")
    print(Circle.__doc__)
    print("\n=== Shape List and Areas ===")
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Rectangle(2, 10),
        Circle(5),
        Rectangle(1, 1)
    ]
    rectangle_count = 0
    circle_count = 0
    for shape in shapes:
        print(shape)
        if isinstance(shape, Rectangle):
            rectangle_count += 1
        elif isinstance(shape, Circle):
            circle_count += 1
    print(f"\nTotal Rectangles: {rectangle_count}")
    print(f"Total Circles: {circle_count}")
