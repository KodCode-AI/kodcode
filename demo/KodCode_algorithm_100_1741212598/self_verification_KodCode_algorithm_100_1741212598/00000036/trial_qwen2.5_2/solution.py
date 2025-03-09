import random
import math

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def construct_route(cities, pheromone_matrix, num_cities, ant_index, alpha, beta):
    """Construct a route for an ant using the probabilistic method."""
    current_city = ant_index
    route = [current_city]
    unvisited_cities = set(range(num_cities)) - {current_city}
    
    while unvisited_cities:
        next_city_probabilities = []
        for next_city in unvisited_cities:
            probability = ((pheromone_matrix[current_city][next_city] ** alpha) *
                           ((1 / calculate_distance(cities[current_city], cities[next_city])) ** beta))
            next_city_probabilities.append((next_city, probability))
        
        next_city, _ = random.choices(next_city_probabilities, weights=[p for _, p in next_city_probabilities])[0]
        route.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city

    return route

def calculate_route_distance(route, cities):
    """Calculate the total distance of a given route."""
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    total_distance += calculate_distance(cities[route[-1]], cities[route[0]])
    return total_distance

def update_pheromone_matrix(pheromone_matrix, routes, q, total_distance, num_cities):
    """Update the pheromone matrix based on the best route found."""
    for route in routes:
        for i in range(num_cities):
            for j in range(num_cities):
                pheromone_matrix[i][j] *= 1 - q / total_distance
                if i != j and (i, j) in [(r, route[i + 1]) for r in range(len(route) - 1)]:
                    pheromone_matrix[i][j] += q / total_distance

def ant_colony_optimization(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q):
    """Execute the main algorithm."""
    num_cities = len(cities)
    pheromone_matrix = [[1 / num_cities for _ in range(num_cities)] for _ in range(num_cities)]
    best_route = []
    best_distance = float('inf')
    
    for _ in range(iterations_num):
        routes = []
        for _ in range(ants_num):
            route = construct_route(cities, pheromone_matrix, num_cities, 0, alpha, beta)
            routes.append(route)
            distance = calculate_route_distance(route, cities)
            if distance < best_distance:
                best_route = route
                best_distance = distance
        update_pheromone_matrix(pheromone_matrix, routes, q, best_distance, num_cities)
    
    return best_route, best_distance

def main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q):
    """Driver function for ACO."""
    return ant_colony_optimization(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)