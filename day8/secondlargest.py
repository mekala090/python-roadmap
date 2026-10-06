# Find the second largest number in a list

numbers = [12, 45, 7, 89, 23, 54, 2, 67]

first = numbers[0]
second = numbers[0]

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("List:", numbers)
print("First largest:", first)
print("Second largest:", second)

# Alternative using sorted()
sorted_numbers = sorted(numbers)
print("Sorted list:", sorted_numbers)
print("Second largest using sorted():", sorted_numbers[-2])
