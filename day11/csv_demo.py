import csv

# Writing
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Asha", 21])
    writer.writerows([["Ravi", 22], ["Meena", 20]])

# Reading
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)                 # each row is a list

# Bonus: DictReader / DictWriter
with open("data.csv") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])