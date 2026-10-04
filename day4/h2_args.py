# Default argument
def power(base, exp=2):
    return base ** exp

print(power(5))       # 25 (uses default exp=2)
print(power(2, 3))    # 8

# Keyword arguments (order doesn't matter)
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

introduce(age=20, city="Nellore", name="Anil")

# *args: any number of positional arguments (arrives as a tuple)
def total(*args):
    s = 0
    for n in args:
        s += n
    return s

print(total(1, 2, 3))
print(total(10, 20, 30, 40, 50))

# **kwargs: any number of keyword arguments (arrives as a dictionary)
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

show_info(name="Sita", age=22, course="Python")

# ---- Day 2 programs rewritten as functions ----
# (Replace/add your own Day 2 programs the same way.)

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c

def calculator(a, b, op="+"):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    return "Invalid operator"

def multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")

print(even_or_odd(7))
print(largest_of_three(4, 9, 6))
print(calculator(10, 5, "*"))
multiplication_table(5)