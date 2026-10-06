# Find the largest and smallest numbers in a list

numbers = [12, 45, 7, 89, 23, 54, 2, 67]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("List:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)

# Another example using built-in functions
print("Using max and min:", max(numbers), min(numbers))
