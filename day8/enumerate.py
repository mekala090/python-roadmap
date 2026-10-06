# Python enumerate() example
# enumerate() adds a counter to an iterable and returns pairs of (index, value)

fruits = ["apple", "banana", "mango", "orange"]

print("Using enumerate without start:")
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\nUsing enumerate with start=1:")
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Example with a list of names
names = ["Karthik", "Priya", "Ravi"]
print("\nNames with index:")
for i, name in enumerate(names):
    print(f"Index {i}: {name}")
