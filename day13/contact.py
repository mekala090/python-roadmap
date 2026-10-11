import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name.lower() in contacts:
        print("Contact already exists.")
        return
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts[name.lower()] = {"name": name, "phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Added {name}.")


def search_contact(contacts):
    query = input("Search name: ").strip().lower()
    results = [c for key, c in contacts.items() if query in key]
    if not results:
        print("No match found.")
        return
    for c in results:
        print(f"{c['name']} | {c['phone']} | {c['email']}")


def delete_contact(contacts):
    name = input("Name to delete: ").strip().lower()
    if name in contacts:
        removed = contacts.pop(name)
        save_contacts(contacts)
        print(f"Deleted {removed['name']}.")
    else:
        print("Contact not found.")


def list_contacts(contacts):
    if not contacts:
        print("Contact book is empty.")
        return
    print(f"\n{'Name':<20}{'Phone':<15}Email")
    print("-" * 50)
    for c in sorted(contacts.values(), key=lambda x: x["name"].lower()):
        print(f"{c['name']:<20}{c['phone']:<15}{c['email']}")


def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add  2. Search  3. Delete  4. List  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            list_contacts(contacts)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()