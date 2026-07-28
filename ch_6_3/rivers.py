rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
    "Mississippi": "United States",
    "Danube": "Germany, Austria, Slovakia, Hungary, Croatia, Serbia, Romania, Bulgaria, Moldova, Ukraine",
}

for river, country in rivers.items():
    print(f"The {river} River runs through {country}.")

for river in rivers.keys():
    print(f"{river} is a major river.")

for country in rivers.values():
    print(f"{country} is a country with a major river.")

