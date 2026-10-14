class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand            # public
        self.model = model            # public
        self._year = year             # _protected: for use by subclasses
        self.__vin = f"VIN-{brand[:2].upper()}{year}"  # __private (name-mangled)

    def get_vin(self):                # getter for the private attribute
        return self.__vin

    def start(self):
        return f"{self.brand} {self.model} is starting..."

    def wheels(self):
        return 4

    def info(self):
        return f"{self._year} {self.brand} {self.model} ({self.wheels()} wheels)"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors=4):
        super().__init__(brand, model, year)   # call parent constructor
        self.doors = doors

    def start(self):                           # method overriding
        return f"{self.brand} {self.model}: Key turned, engine roars!"

    def info(self):
        return super().info() + f", {self.doors} doors"


class Bike(Vehicle):
    def __init__(self, brand, model, year, has_gear=True):
        super().__init__(brand, model, year)
        self.has_gear = has_gear

    def wheels(self):                          # overriding
        return 2

    def start(self):                           # overriding
        return f"{self.brand} {self.model}: Kick-start! Vroom!"

    def info(self):
        gear = "geared" if self.has_gear else "gearless"
        return super().info() + f", {gear}"


class ElectricCar(Car):                        # multilevel: Vehicle -> Car -> ElectricCar
    def __init__(self, brand, model, year, battery_kwh, doors=4):
        super().__init__(brand, model, year, doors)
        self.battery_kwh = battery_kwh

    def start(self):
        return f"{self.brand} {self.model}: Silent start... (no engine noise)"

    def info(self):
        return super().info() + f", {self.battery_kwh} kWh battery"
if __name__ == "__main__":
    print("=== Vehicle Hierarchy ===")
    vehicles = [
        Car("Toyota", "Camry", 2022),
        Bike("Yamaha", "R15", 2023),
        ElectricCar("Tesla", "Model 3", 2024, battery_kwh=75),
    ]
    for v in vehicles:                         # polymorphism
        print(v.start())
        print(" ", v.info())

    car = vehicles[0]
    print("\nVIN via getter:", car.get_vin())
    print("Protected (accessible, but by convention don't):", car._year)
    try:
        print(car.__vin)
    except AttributeError as e:
        print("Private access error:", e)
    print("Name-mangled access (not recommended):", car._Vehicle__vin)

    ev = vehicles[2]
    print("\nisinstance:", isinstance(ev, Car), isinstance(ev, Vehicle), isinstance(ev, Bike))
    print("MRO:", [c.__name__ for c in ElectricCar.__mro__])