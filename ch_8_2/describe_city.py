def describe_city(city, country='China'):
    """Display a simple message about a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('Beijing')
describe_city(city = 'Shanghai')
describe_city('New York', 'USA')
describe_city('Los Angeles', country = 'USA')
describe_city(city = 'Washington', country = 'USA')
describe_city(city = 'London', country = 'UK')

