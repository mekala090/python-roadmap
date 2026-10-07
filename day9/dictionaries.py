d = {"apple": 3, "banana": 5}
d["cherry"] = 7
d.update({"kiwi": 2, "apple": 10})
print(d.keys(), d.values(), d.items())
print(d.get("mango", 0))    # 0, no KeyError

for k, v in d.items():
    print(k, v)

squares = {n: n**2 for n in range(1, 6)}
filtered = {k: v for k, v in d.items() if v > 2}
inverted = {v: k for k, v in d.items()}
from_lists = dict(zip(["a", "b", "c"], [1, 2, 3]))
print(squares, filtered, inverted, from_lists)
