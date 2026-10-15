import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def exercise_1():
    print("\n=== Exercise 1: Shape abstract class ===")
    shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
    for s in shapes:
        print(s)  # polymorphism: each shape computes its own area
    print("Total area:", round(sum(s.area() for s in shapes), 2))


if __name__ == "__main__":
    exercise_1()
 