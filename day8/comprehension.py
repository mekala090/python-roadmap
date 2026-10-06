# List Comprehensions Examples

# 1. Squares of numbers
squares = [x**2 for x in range(6)]
print("Squares:", squares)   # [0, 1, 4, 9, 16, 25]

# 2. Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)   # [0, 2, 4, 6, 8]

# 3. Odd numbers only
odds = [x for x in range(10) if x % 2 != 0]
print("Odd numbers:", odds)   # [1, 3, 5, 7, 9]

# 4. Convert strings to uppercase
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", upper_fruits)   # ['APPLE', 'BANANA', 'CHERRY']

# 5. Filter words longer than 5 letters
words = ["cat", "elephant", "dog", "giraffe"]
long_words = [w for w in words if len(w) > 5]
print("Words longer than 5 letters:", long_words)   # ['elephant', 'g