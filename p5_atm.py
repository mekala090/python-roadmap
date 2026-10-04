balance = 10000
pin = 1234

entered = int(input("Enter PIN: "))

if entered != ______:
    print("Wrong PIN")
else:
    amount = float(input("Enter amount to withdraw: "))
    if amount ______ 0:
        print("Invalid amount")
    elif amount ______ balance:
        print("Insufficient funds")
    else:
        print(f"Withdrawn {amount}. New balance: {balance - amount}")