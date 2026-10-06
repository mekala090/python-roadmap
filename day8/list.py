numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

numbers.append(6)
print("After append:", numbers)

numbers.insert(2, 10)
print("After insert:", numbers)

numbers.remove(10)
print("After remove:", numbers)

popped = numbers.pop()
print("After pop:", numbers)
print("Popped value:", popped)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Length of list:", len(numbers))
