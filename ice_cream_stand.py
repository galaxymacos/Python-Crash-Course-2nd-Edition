from restaurant import *


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(f"This ice cream stand is making {self.flavors} ice cream")

        
ice_cream_stand = IceCreamStand("Hotel", "Chinese", "Strawberry")
ice_cream_stand.show_flavors()
