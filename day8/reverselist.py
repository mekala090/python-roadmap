# Reverse a list in Python

numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

# Method 1: using reverse()
reversed_numbers = numbers.copy()
reversed_numbers.reverse()
print("Reversed using reverse():", reversed_numbers)

# Method 2: using slicing
reversed_slice = numbers[::-1]
print("Reversed using slicing:", reversed_slice)

# Method 3: manual reverse using loop
manual_reverse = []
for value in numbers:
    manual_reverse.insert(0, value)
print("Reversed manually:", manual_reverse)

# Example with strings
names = ["Alice", "Bob", "Charlie"]
print("Original names:", names)
print("Reversed names:", names[::-1])
