destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for i in destinations]
attractions_with_interest = []

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    test_destination = traveler[1]
    traveler_destination_index = get_destination_index(test_destination)
    return traveler_destination_index

def add_attraction(destination,attraction):
    try:
        destination_index = destinations.index(destination)
        attraction_for_destination = attractions[destination_index].append(attraction)
        return attraction_for_destination
    except SyntaxError:
        return

def find_attractions(destination,interests):
    destination_index = destinations.index(destination)
    for possible_attraction in interests:
  	     attractions_in_city = attractions[destination_index]
         attraction_tags = attractions_in_city[1]
         for interest in interests
            if attraction_tags == interest:
                attraction_tags
            else:
                continue




add_attraction('Los Angeles, USA',['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)
