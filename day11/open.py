# "w" - write (creates the file, or overwrites if it exists)
with open("notes.txt", "w") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: Python\n")

# "a" - append (adds to the end, never erases)
with open("notes.txt", "a") as f:
    f.write("Line 3: File handling\n")

# "r" - read (default mode; file must exist)
with open("notes.txt", "r") as f:
    content = f.read()          # whole file as one string
print(content)

# readline() - one line at a time
with open("notes.txt", "r") as f:
    first = f.readline()
    second = f.readline()
print(first.strip(), "|", second.strip())

# Loop over lines (best for big files)
with open("notes.txt") as f:
    for line in f:
        print(line.strip())

# readlines() - all lines as a list
with open("notes.txt") as f:
    lines = f.readlines()
print(lines)

# Why "with"? It closes the file automatically, even if an error occurs.