t = (10, 20, 30)
a, b, c = t                 # unpacking
first, *rest = t            # first=10, rest=[20, 30]
a, b = b, a                 # swap

def stats(nums):
    return min(nums), max(nums), sum(nums)

mn, mx, total = stats([4, 8, 1, 9])
print(mn, mx, total)        # 1 9 22
