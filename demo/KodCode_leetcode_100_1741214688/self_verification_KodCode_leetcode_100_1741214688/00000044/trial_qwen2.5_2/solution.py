from collections import defaultdict
from heapq import heappush, heappop

def find_cheapest_itinerary(flights, reservations):
    """
    Finds the cheapest valid itinerary visiting every city exactly once. If no such itinerary exists, returns -1.
    """
    graph = defaultdict(list)
    for i, j, k in flights:
        graph[i].append((j, k))
    
    start = None
    reservation_map = defaultdict(list)
    for i, j in reservations:
        reservation_map[i].append(j)
    
    def dfs(city, visited, path, cost, cities):
        nonlocal cheapest_cost, cheapest_path
        
        if len(visited) == len(cities):
            if cost < cheapest_cost or (cost == cheapest_cost and ''.join(map(str, path)) < ''.join(map(str, cheapest_path))):
                cheapest_cost, cheapest_path = cost, path.copy()
            return
        
        for next_city, flight_cost in graph[city]:
            if next_city in visited:
                continue
            if next_city not in reservation_map[city] and next_city not in visited:
                continue
            visited.add(next_city)
            path.append(next_city)
            dfs(next_city, visited, path, cost + flight_cost, cities)
            path.pop()
            visited.remove(next_city)
    
    cities = list(reservation_map.keys())
    cheapest_cost, cheapest_path = float('inf'), []
    for city in cities:
        visited = set([city])
        path = [city]
        dfs(city, visited, path, 0, cities)
    
    return cheapest_cost if cheapest_cost != float('inf') else -1