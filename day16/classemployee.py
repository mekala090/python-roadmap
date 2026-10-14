class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self._emp_id = emp_id        # _protected
        self.__salary = 0            # __private
        self.salary = salary         # goes through the setter (validation)

    @property
    def salary(self):                # getter
        return self.__salary

    @salary.setter
    def salary(self, value):         # setter with validation
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value

    @property
    def emp_id(self):                # read-only property (no setter)
        return self._emp_id

    def annual_salary(self):
        return self.__salary * 12

    def details(self):
        return f"[{self._emp_id}] {self.name} | Monthly salary: {self.salary:,.2f}"


class Manager(Employee):
    def __init__(self, name, emp_id, salary, team=None, bonus_percent=10):
        super().__init__(name, emp_id, salary)
        self.team = team if team is not None else []
        self.__bonus_percent = bonus_percent

    def add_member(self, employee):
        self.team.append(employee)

    def annual_salary(self):                   # overriding: adds a bonus
        base = super().annual_salary()
        return base + base * self.__bonus_percent / 100

    def details(self):
        return super().details() + f" | Team size: {len(self.team)}"


if __name__ == "__main__":
    print("\n=== Employee -> Manager ===")
    e1 = Employee("Asha", "E101", 40000)
    e2 = Employee("Ravi", "E102", 45000)
    m = Manager("Sneha", "M001", 90000, bonus_percent=15)
    m.add_member(e1)
    m.add_member(e2)

    print(e1.details(), "| Annual:", f"{e1.annual_salary():,.2f}")
    print(m.details(), "| Annual (with bonus):", f"{m.annual_salary():,.2f}")

    m.salary = 95000                           # setter via property
    print("After raise:", m.salary)

    for bad in (-500, "lots"):
        try:
            m.salary = bad
        except (ValueError, TypeError) as e:
            print(f"Rejected {bad!r}: {e}")

    try:
        m.emp_id = "X999"                      # read-only property
    except AttributeError as e:
        print("emp_id is read-only:", e)