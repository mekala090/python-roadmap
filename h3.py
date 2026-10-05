def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

def remove_spaces(s):
    return s.replace(" ", "")

def capitalize_words(s):
    words = s.split()
    result = []
    for w in words:
        result.append(w.capitalize())
    return " ".join(result)

def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

def longest_word(s):
    longest = ""
    for w in s.split():
        if len(w) > len(longest):
            longest = w
    return longest

def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

# Tests
print(reverse_string("hello"))
print(is_palindrome("Madam"))
print(count_vowels("education"))
print(remove_spaces("a b c"))
print(capitalize_words("hello world"))
print(is_anagram("listen", "silent"))
print(longest_word("I love programming"))
print(char_frequency("hello"))