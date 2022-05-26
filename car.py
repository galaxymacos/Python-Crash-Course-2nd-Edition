class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, mile):
        self.odometer += mile


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
