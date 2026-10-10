flight_route = [
    ("New Orleans", "Houston"),
    ("Houston", "Denver"),
    ("Denver", "Seattle"),
]


def print_itinerary(route_list):
    print("Flight Itinerary")
    flight_number = 1
    for departure_city, arrival_city in route_list:
        print(f"Flight {flight_number}: {departure_city} -> {arrival_city}")
        flight_number += 1


if __name__ == "__main__":
    print_itinerary(flight_route)
