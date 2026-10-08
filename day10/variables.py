a = [1, 2, 3]
b = a            # same object, two names
b.append(4)
print(a)         # [1,2,3,4]
print(a is b)    # True
print(id(a), id(b))