
import math
from abc import ABC, abstractmethod
 
 
# =====================================================================
# H1: POLYMORPHISM, DUCK TYPING, DUNDER METHODS
# =====================================================================
 
# --- Polymorphism: same method name, different behaviour per class ---
class Dog:
    def speak(self):
        return "Woof"
 
 
class Cat:
    def speak(self):
        return "Meow"
 
 
# --- Duck typing: "if it quacks like a duck..." No shared base class needed ---
class Robot:
    def speak(self):
        return "Beep boop"
 
 
def make_it_speak(thing):
    # Doesn't care about the type, only that it has .speak()
    print(thing.speak())
 
 
# --- Dunder methods: __str__, __repr__, __eq__, __len__ ---
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
 
    def __str__(self):
        # Human-friendly, used by print() and str()
        return f"'{self.title}' by {self.author}"
 
    def __repr__(self):
        # Developer-friendly, ideally recreates the object
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"
 
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title, self.author) == (other.title, other.author)
 
    def __len__(self):
        # len(book) -> number of pages
        return self.pages
# Add this at the end of the file
if __name__ == "__main__":
    d = Dog()
    c = Cat()
    r = Robot()

    print(d.speak())   # Woof
    print(c.speak())  # Meow
    print(r.speak())  # Beep boop

    b = Book("Python Basics", "Karthik", 250)
    print(str(b))     # 'Python Basics' by Karthik
    print(repr(b))
    print(len(b))     # 250