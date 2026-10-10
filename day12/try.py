def demo(a, b):
    try:
        result = int(a) / int(b)
    except ValueError:
        print("Error: please enter valid integers.")
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Done (finally always runs).")

demo("10", "2")
demo("abc", "2")
demo("10", "0")

# FileNotFoundError
try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")