age = 25
has_id = True

print(age >= 18 and has_id)    # True only if BOTH are True
print(age < 18 or has_id)      # True if AT LEAST ONE is True
print(not has_id)              # flips True to False