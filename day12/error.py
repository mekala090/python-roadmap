class InvalidOperatorError(Exception):
    pass

def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b  # may raise ZeroDivisionError
    else:
        raise InvalidOperatorError(f"Invalid operator: '{op}'. Use + - * /")

def main():
    while True:
        try:
            a = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ").strip()
            b = float(input("Enter second number: "))
            result = calculate(a, b, op)
        except ValueError:
            print("Error: please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: cannot divide by zero.")
        except InvalidOperatorError as e:
            print("Error:", e)
        else:
            print(f"Result: {result}")
        finally:
            print("-" * 30)

        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

main()