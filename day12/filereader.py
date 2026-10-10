def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: no permission to read '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: '{filename}' is not a readable text file.")
    return None

name = input("Enter file name: ")
content = read_file(name)
if content is not None:
    print("File contents:")
    print(content)