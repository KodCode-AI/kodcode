from collections import defaultdict
from itertools import permutations

def cheapest_itinerary(flights, reservations):
    """
    Returns the total cost of the cheapest valid itinerary that visits every city exactly once.
    """
    # Build the graph and filter out invalid reservations
    graph = defaultdict(dict)
    for i, j, k in flights:
        graph[i][j] = k
    valid_reservations = [[i, j] for i, j in reservations if j in graph[i]]
    
    # Check if there are enough flights to cover reservations
    if len(valid_reservations) != len(reservations):
        return -1
    
    # Generate all possible itineraries
    itineraries = []
    for perm in permutations(range(len(flights))):
        itinerary = [i for i in range(len(flights))]
        for i in range(len(perm)):
            if perm[i] != i and itinerary[perm[i]] != itinerary[i]:
                break
        else:
            itineraries.append(itinerary)
    
    # Calculate the total cost for each valid itinerary
    costs = [sum(graph[from_city][to_city] for from_city, to_city in zip(itinerary, itinerary[1:])) for itinerary in itineraries if all(graph[from_city][to_city] for from_city, to_city in zip(itinerary, itinerary[1:]))]
    
    # Return the cheapest valid itinerary or -1 if none exist
    if costs:
        min_cost = min(costs)
        min_index = costs.index(min_cost)
        return min_cost, itineraries[min_index]
    return -1