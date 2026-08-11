favorite_places = {
    'alice': ['paris', 'new york', 'tokyo'],
    'bob': ['london', 'berlin', 'sydney'],
    'charlie': ['rome', 'barcelona', 'amsterdam'],
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
