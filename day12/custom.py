class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed."""
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot take the square root of a negative number.")
    return n ** 0.5

try:
    print(square_root(16))
    print(square_root(-4))
except NegativeNumberError as e:
    print("Custom error:", e)