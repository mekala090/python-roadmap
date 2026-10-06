# Nested Loops with Lists Examples

# 1. Simple nested loop to create pairs
pairs = []
for x in [1, 2, 3]:
    for y in [4, 5]:
        pairs.append((x, y))
print("Pairs using nested loops:", pairs)
# [(1,4), (1,5), (2,4), (2,5), (3,4), (3,5)]

# 2. Nested loop with condition
pairs_even = []
for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        if (x + y) % 2 == 0:
            pairs_even.append((x, y))
print("Pairs with even sum:", pairs_even)

# 3. Nested loop to multiply elements
products = []
for a in [2, 3]:
    for b in [10, 20]:
        products.append(a * b)
print("Products:", products)   # [20, 40, 30, 60]

# 4. Nested loop with strings
words1 = ["red", "blue"]
words2 = ["car", "house"]
combinations = []
for w1 in words1:
    for w2 in words2:
        combinations.append(w1 + " " + w2)
print("Word combinations:", combinations)
# ['red car', 'red house', 'blue car', 'blue house']
