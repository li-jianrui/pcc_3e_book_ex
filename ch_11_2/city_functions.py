def city_country(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()} - Population {population}"
    else:
        return f"{city.title()}, {country.title()}"