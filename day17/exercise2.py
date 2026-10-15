from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name
 
    @abstractmethod
    def sound(self):
        pass
 
    def speak(self):
        return f"{self.name} says {self.sound()}"
 
 
class DogA(Animal):
    def sound(self):
        return "Woof!"
 
 
class CatA(Animal):
    def sound(self):
        return "Meow!"
 
 
class Cow(Animal):
    def sound(self):
        return "Moo!"
 
 
class Duck(Animal):
    def sound(self):
        return "Quack!"
 
 
def exercise_2():
    print("\n=== Exercise 2: Animal sounds ===")
    zoo = [DogA("Buddy"), CatA("Whiskers"), Cow("Daisy"), Duck("Donald")]
    for animal in zoo:
        print(animal.speak())


if __name__ == "__main__":
    exercise_2()
 