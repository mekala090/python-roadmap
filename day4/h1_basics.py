# 1. Function with no parameters
def greet():
    print("Hello, welcome to Day 4!")

# 2. Function with parameters
def greet_person(name):
    print("Hello,", name)

# 3. Function with return and a docstring
def add(a, b):
    """Return the sum of a and b."""
    return a + b

# 4. Return vs print
def square(n):
    """Return the square of n."""
    return n * n

# ---- Calling the functions ----
greet()
greet_person("Ravi")

result = add(10, 20)
print("Sum:", result)

print("Square of 7:", square(7))

# Docstring access
print(add.__doc__)
print(square.__doc__)