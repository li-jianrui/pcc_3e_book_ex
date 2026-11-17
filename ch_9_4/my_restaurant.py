from restaurant import Restaurant

my_restaurant = Restaurant("The Great Eatery", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.print_number_served()
my_restaurant.number_served = 5
my_restaurant.print_number_served()
my_restaurant.set_number_served(10)
my_restaurant.print_number_served()
my_restaurant.increment_number_served(5)
my_restaurant.print_number_served()