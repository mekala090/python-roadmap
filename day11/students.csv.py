import csv

with open("students.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "marks"])
    w.writerows([["Asha", 88], ["Ravi", 92], ["Meena", 79], ["Kiran", 85]])

import csv

topper_name = ""
top_marks = -1

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        marks = int(row["marks"])
        if marks > top_marks:
            top_marks = marks
            topper_name = row["name"]

print(f"Topper: {topper_name} with {top_marks} marks")
# Output: Topper: Ravi with 92 marks