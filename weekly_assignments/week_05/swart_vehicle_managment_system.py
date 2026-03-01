class Vehicle:
    def __init__(self, b, s, f):
        self.brand = b
        self.speed = s
        self.fuel = f
    def display_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)
        print("Fuel Type:", self.fuel)
class Car(Vehicle):
    def __init__(self, b, s, f, d):
        super().__init__(b, s, f)
        self.doors = d
    def display_info(self):
        super().display_info()
        print("Doors:", self.doors)
class Bike(Vehicle):
    def __init__(self, b, s, f, e):
        super().__init__(b, s, f)
        self.engine = e
    def display_info(self):
        super().display_info()
        print("Engine Capacity:", self.engine)
c = Car ("Toyota", 120, "Petrol", 4)
b = Bike("Yamaha", 100, "Petrol", "150cc")
print("Car Details:")
c.display_info()
print("\nBike Details:")
b.display_info()
