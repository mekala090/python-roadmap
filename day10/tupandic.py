pairs = [("amy", 80), ("bob", 95), ("cat", 80)]
sorted(pairs, key=lambda p: p[1])               # by score
sorted(pairs, key=lambda p: (-p[1], p[0]))      # score desc, then name asc

students = [{"name": "amy", "marks": 80}, {"name": "bob", "marks": 95}]
sorted(students, key=lambda s: s["marks"], reverse=True)

d = {"a": 3, "b": 1}
sorted(d.items(), key=lambda kv: kv[1])         # sort dict by value