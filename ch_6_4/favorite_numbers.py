favorite_numbers = {
    "Alice" : [1, 2, 3],
    "Bob" : [2, 4, 6],
    "Charlie" : [3, 6, 9],
    "David" : [4, 8, 12],
    "Eve" : [5, 10, 15],
    }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
