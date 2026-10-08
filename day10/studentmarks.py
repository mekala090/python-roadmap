students = [
    {"name": "Mia", "marks": 88},
    {"name": "Noah", "marks": 95},
    {"name": "Ivy", "marks": 81},
]

ranked_students = sorted(
    students, key=lambda student: student["marks"], reverse=True
)

for rank, student in enumerate(ranked_students, start=1):
    print(f"{rank}. {student['name']} - {student['marks']} marks")

words = ["pear", "fig", "plum", "apple", "kiwi"]
sorted_words = sorted(words, key=lambda word: (len(word), word))
print(sorted_words)