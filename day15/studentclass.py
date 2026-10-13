class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def display(self):
        print(f"Name: {self.name} | Roll: {self.roll} | Marks: {self.marks} | Average: {self.average():.2f}")


print("\n===== H2: Student =====")
s1 = Student("Asha", 101, [85, 90, 78])
s2 = Student("Ravi", 102, [70, 65, 80])
s3 = Student("Meena", 103, [95, 92, 98])
for s in (s1, s2, s3):
    s.display()