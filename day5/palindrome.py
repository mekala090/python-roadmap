def is_palindrome(n):
    original, rev = n, 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return original == rev