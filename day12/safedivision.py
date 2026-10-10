def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
    except TypeError:
        print("Error: both values must be numbers.")
    return None

try:
    x = float(input("Enter numerator: "))
    y = float(input("Enter denominator: "))
except ValueError:
    print("Error: please enter valid numbers.")
else:
    result = safe_divide(x, y)
    if result is not None:
        print(f"{x} / {y} = {result}")