nums = [5, 2, 9, 1]
new = sorted(nums) # returns a NEW list, original unchanged
print(nums, new) # [5,2,9,1] [1,2,5,9]

r = nums.sort() # sorts IN PLACE, returns None
print(nums, r) # [1,2,5,9]