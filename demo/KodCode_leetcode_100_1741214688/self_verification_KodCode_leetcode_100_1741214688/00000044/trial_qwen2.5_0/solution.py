from collections import defaultdict
from itertools import permutations

def cheapest_itinerary(flights, reservations):
    """
    Returns the total cost of the cheapest valid itinerary that visits every city exactly once,
    or -1 if no such itinerary exists.
    """
    # Create a graph from the flights list
    graph = defaultdict(list)
    for i, j, k in flights:
        graph[i].append((j, k))
        graph[j].append((i, k))
    
    # Filter out airports where no direct flights are made according to reservations
    airports = set()
    for i, j in reservations:
        airports.add(i)
        airports.add(j)
    airports = list(airports)
    
    # Find all possible permutations of the itinerary
    min_cost = float('inf')
    best_path = []
    for perm in permutations(airports):
        current_cost = 0
        valid = True
        for i in range(len(perm) - 1):
            u, v = perm[i], perm[i + 1]
            if (u, v) in graph and (v, u) in graph:
                for j, k in graph[u]:
                    if j == v:
                        current_cost += k
                        break
                else:
                    valid = False
                    break
            elif (v, u) in graph:
                for j, k in graph[v]:
                    if j == u:
                        current_cost += k
                        break
                else:
                    valid = False
                    break
        
        if valid and current_cost < min_cost:
            min_cost = current_cost
            best_path = perm
    
    return min_cost if min_cost != float('inf') else -1