import json

FILE = "todo.json"

def save_todos(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f, indent=4)

def load_todos():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

todos = load_todos()
todos.append({"task": "Learn file handling", "done": False})
todos.append({"task": "Practice csv module", "done": True})
save_todos(todos)

# Reload and display
for i, t in enumerate(load_todos(), 1):
    status = "✔" if t["done"] else "✘"
    print(f"{i}. [{status}] {t['task']}")