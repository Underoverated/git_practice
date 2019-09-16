destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', 'historical site', 'art']

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

def add_attraction(destination,attraction):
    try:
        destination_index = get_destination_index(destination)
    except:
        return
    attractions_for_destination = [[destination,attraction] for destination in destinations]
    return attractions_for_destination

attractions = [[] for destination in destinations]

test_destination_index = get_traveler_location(test_traveler)

print(add_attraction(destinations,'beach'))
