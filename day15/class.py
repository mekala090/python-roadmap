class Dog:
    species = "Canis familiaris"      # class attribute (shared)

    def __init__(self, name, age):
        self.name = name              # instance attributes (unique)
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")


print("===== H1: Basics =====")
d1 = Dog("Buddy", 3)
d2 = Dog("Max", 5)
d1.bark()
d2.bark()
print(d1.name, d1.age, d1.species)
print(d2.name, d2.age, d2.species)

Dog.species = "Dog (updated)"         # changes for all objects
print(d1.species, "|", d2.species)

d1.species = "Special Dog"            # only d1 gets its own copy
print(d1.species, "|", d2.species)