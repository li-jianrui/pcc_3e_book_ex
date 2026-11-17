class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    def print_number_served(self):
        print(f"{self.restaurant_name} has served {self.number_served} customers.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def show_flavors(self):
        print(f"{self.restaurant_name} offers the following flavors: {', '.join(self.flavors)}")

ice_cream_stand = IceCreamStand("Sweet Treats")
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.show_flavors()