def city_country(city, country):
    """Return a string in the format 'City, Country'."""
    return f"{city.title()}, {country.title()}"

print(city_country('beijing', 'china'))
print(city_country('shanghai', 'china'))
print(city_country('new york', 'usa'))