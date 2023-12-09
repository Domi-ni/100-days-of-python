country = input("add the name of the country: ")  # Add country name
visits = int(input(f"how many times did you visted {country}?: "))
list_of_cities = input(
    "wich cities have you visited? separete them with a coma and a space: "
)
list_of_cities = list_of_cities.split(", ")

travel_log = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def add_new_country(country_visited, number_of_visits, cities_visited):
    travel_log.append(
        {
            "country": country_visited,
            "visits": number_of_visits,
            "cities": cities_visited,
        }
    )


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
