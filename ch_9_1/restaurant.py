class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

restaurant = Restaurant("The Great Eatery", "Italian")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant("Sushi World", "Japanese")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant("Taco Fiesta", "Mexican")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3 = Restaurant("Burger Haven", "American")
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
