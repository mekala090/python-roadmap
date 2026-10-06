# Indexing examples
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Access by position
print("First element:", numbers[0])      # 10
print("Second element:", numbers[1])     # 20
print("Last element:", numbers[-1])      # 50
print("Second last element:", numbers[-2]) # 40

# Change a value using index
numbers[2] = 99
print("After changing 3rd element:", numbers)

# Using index inside a loop
for i in range(len(numbers)):
    print(f"Index {i} → Value {numbers[i]}")
