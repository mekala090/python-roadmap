s = {1, 2, 2, 3}            # {1, 2, 3}
s.add(4)
s.discard(10)               # no error if missing
x = {1, 2, 3, 4}
y = {3, 4, 5}
print(x | y)                # union
print(x & y)                # intersection
print(x - y)                # difference
print(x ^ y)                # symmetric difference
print(list(set([1, 1, 2, 3, 3])))   # remove duplicates
