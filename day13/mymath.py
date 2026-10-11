def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def main():
    print("Testing mymath directly")
    print(add(2, 3))
    print(multiply(4, 5))

# Runs only when you execute `python mymath.py`,
# NOT when another file imports it.
if __name__ == "__main__":
    main()