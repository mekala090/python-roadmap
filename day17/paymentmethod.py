from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        """Every subclass MUST implement this."""


class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount:.2f} by credit card"


class UPI(PaymentMethod):
    def pay(self, amount):
        return f"Paid INR {amount:.2f} via UPI"


class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    # @classmethod: receives the class (cls), often used as an alternative constructor
    @classmethod
    def from_birth_year(cls, name, birth_year, current_year=2026):
        return cls(name, current_year - birth_year)

    @classmethod
    def get_population(cls):
        return cls.population

    # @staticmethod: no self / cls, just a utility grouped with the class
    @staticmethod
    def is_adult(age):
        return age >= 18

    def __repr__(self):
        return f"Person({self.name!r}, {self.age})"


def demo_h2():
    print("\n=== H2: Abstract classes ===")
    try:
        PaymentMethod()
    except TypeError as e:
        print("Cannot instantiate abstract class:", e)
    for method in (CreditCard(), UPI()):
        print(method.pay(250))

    print("\n=== H2: classmethod & staticmethod ===")
    p1 = Person("Asha", 30)
    p2 = Person.from_birth_year("Ravi", 2000)  # alternative constructor
    print(p1, p2)
    print("Population:", Person.get_population())
    print("Is 17 an adult?", Person.is_adult(17))


if __name__ == "__main__":
    demo_h2()