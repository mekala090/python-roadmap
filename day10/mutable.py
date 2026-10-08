s = "hi"
s += "!"         # creates a NEW string
t = (1, [2, 3])
t[1].append(4)   # works! the tuple holds a reference to a mutable list
# t[0] = 9       # TypeError

students = [
    {"name": "Ava", "marks": 85},
    {"name": "Ben", "marks": 92},
    {"name": "Cara", "marks": 78},
]
sorted_students = sorted(
    students, key=lambda s: s["marks"], reverse=True
)
print(sorted_students)