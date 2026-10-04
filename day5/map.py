nums = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(squares, evens)