nums = [5, 2, 9, 1]
new = sorted(nums, reverse=True)  # returns a NEW list, original unchanged
print(nums, new)                  # [5,2,9,1] [9,5,2,1]

r = nums.sort(reverse=True)  # sorts IN PLACE, returns None
print(nums, r)               # [9,5,2,1] None