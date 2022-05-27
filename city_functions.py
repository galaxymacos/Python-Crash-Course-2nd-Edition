def city_country(city, country, population=None):
    if population:
        return city.title() + ", " + country.title() + "-" + " population "+population
    else:
        return city.title() + ", " + country.title()