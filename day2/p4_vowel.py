ch = input("Enter a character: ").lower()

if not ch.isalpha() or len(ch) != 1:
    print("Not a single letter")
elif ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")