buffet_tuple = ("salad", "soup", "breadsticks", "pasta", "dessert")
print("Original buffet menu:")
for item in buffet_tuple:
    print(item)

# buffet_tuple[1] = "clam chowder"  # This will raise a TypeError because tuples are immutable

buffet_tuple = ("salad", "soup", "fish", "noodle", "dim sum")
print("\nUpdated buffet menu:")
for item in buffet_tuple:
    print(item)