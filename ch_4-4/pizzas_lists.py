my_pizzas = ["Margherita", "Pepperoni", "Hawaiian"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("Veggie")
friend_pizzas.append("BBQ Chicken")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)