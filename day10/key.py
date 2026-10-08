words = ["banana", "fig", "apple"]
sorted(words, key=len) # ['fig', 'apple', 'banana']
sorted(words, key=str.lower) # case-insensitive
sorted(words, key=lambda w: w[-1]) # by last letter . fIx this code













