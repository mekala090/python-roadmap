class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120."):
        self.age = age
        self.message = message
        super().__init__(f"{message} (got {age})")

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return age

while True:
    try:
        age = int(input("Enter your age: "))
        validate_age(age)
    except ValueError:
        print("Please enter a valid whole number.")
    except InvalidAgeError as e:
        print("Error:", e)
    else:
        print(f"Valid age: {age}")
        break