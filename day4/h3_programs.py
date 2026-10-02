def factorial(n):
    """Return n! (n factorial)."""
    if n < 0:
        return None          # factorial not defined for negatives
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """Return True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def count_digits(n):
    """Return the number of digits in n."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def reverse_number(n):
    """Return the digits of n reversed (e.g. 123 -> 321)."""
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def sum_of_digits(n):
    """Return the sum of digits of n (e.g. 123 -> 6)."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# ---- Testing ----
num = int(input("Enter a number: "))

print("Factorial:", factorial(num))
print("Is prime:", is_prime(num))
print("First", num, "Fibonacci numbers:", fibonacci(num))
print("Digit count:", count_digits(num))
print("Reversed:", reverse_number(num))
print("Sum of digits:", sum_of_digits(num))