# Slicing examples
numbers = [10, 20, 30, 40, 50, 60, 70]
print("Original list:", numbers)

# Basic slices
print("First three elements:", numbers[:3])       # [10, 20, 30]
print("From index 2 to 5:", numbers[2:6])         # [30, 40, 50, 60]
print("From index 3 to end:", numbers[3:])        # [40, 50, 60, 70]

# Negative indices with slicing
print("Last two elements:", numbers[-2:])         # [60, 70]
print("All except last two:", numbers[:-2])       # [10, 20, 30, 40, 50]

# Step slicing
print("Every second element:", numbers[::2])      # [10, 30, 50, 70]
print("Reverse list using slicing:", numbers[::-1]) # [70, 60, 50, 40, 30, 20, 10]

# Custom step
print("From index 1 to 6, step 2:", numbers[1:6:2]) # [20, 40, 60]
