def factorial(n):
    print("calling", n)
    if n <= 1:
        print("base case reached")
        return 1
    result = n * factorial(n - 1)
    print("returning", result, "for n =", n)
    return result

factorial(5)