def get_integer(prompt):
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except EOFError:
            print("\nInput closed. Exiting.")
            raise SystemExit


num = get_integer("Enter an integer: ")
print(f"You entered: {num}")