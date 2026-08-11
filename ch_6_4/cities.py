new_york = {
    "country": "USA",
    "population": 8419000,
    "fact": "New York is known as the Big Apple."
}

london = {
    "country": "UK",
    "population": 8982000,
    "fact": "London is known for its historic landmarks like the Tower of London and Buckingham Palace."
}

paris = {
    "country": "France",
    "population": 2148000,
    "fact": "Paris is known as the City of Light."
}

beijing = {
    "country": "China",
    "population": 21540000,
    "fact": "Beijing is known for its historical sites like the Forbidden City and Tiananmen Square."
}

cities = {
    "New York": new_york,
    "London": london,
    "Paris": paris,
    "Beijing": beijing
}

for city, info in cities.items():
    print(f"{city} is in {info['country']}.")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}\n")
