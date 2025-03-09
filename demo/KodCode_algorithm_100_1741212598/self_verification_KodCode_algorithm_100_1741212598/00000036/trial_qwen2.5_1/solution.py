import random
import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def initialize_pheromones(cities_num):
    return np.ones((cities_num, cities_num))

def ant_surprise(pid, pheromone, city_map, visited_cities, unvisited_cities):
    probabilities = (pheromone[visited_cities, unvisited_cities] ** alpha) * (1 / city_map[visited_cities, unvisited_cities] ** beta)
    probabilities /= probabilities.sum(axis=1, keepdims=True)
    next_city = np.random.choice(unvisited_cities, p=probabilities[-1])
    return next_city

def calculate_total_distance(path, city_map):
    return sum(city_map[path[i % len(path)], path[(i + 1) % len(path)]) for i in range(len(path)))

def main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q):
    cities_num = len(cities)
    cities_index = list(cities.keys())
    city_map = [[calculate_distance(cities[city1], cities[city2]) for city2 in cities] for city1 in cities]
    pheromone = initialize_pheromones(cities_num)

    best_path = None
    best_distance = float("inf")
    
    for _ in range(iterations_num):
        routes = []
        for _ in range(ants_num):
            route = [cities_index[0]]
            unvisited_cities = [city for city in cities_index[1:]]
            while unvisited_cities:
                next_city = ant_surprise(len(route), pheromone, city_map, route, unvisited_cities)
                route.append(next_city)
                unvisited_cities.remove(next_city)
            route.append(cities_index[0])  # Return to the starting city
            routes.append(route)
            total_distance = calculate_total_distance(route, city_map)
            if total_distance < best_distance:
                best_distance = total_distance
                best_path = route
            pheromone *= (1 - pheromone_evaporation)
            for i in route[:-1]:
                pheromone[i, route[route.index(i) + 1]] += q / city_map[i, route[route.index(i) + 1]]
                pheromone[route[route.index(i) + 1], i] += q / city_map[route[route.index(i) + 1], i]
    
    return best_path, best_distance

# Example usage
cities = {
    0: [0, 0],
    1: [0, 5],
    2: [3, 8],
    3: [8, 10],
    4: [12, 12],
    5: [18, 10],
    6: [15, 5],
    7: [20, 0]
}
ants_num = 10
iterations_num = 100
pheromone_evaporation = 0.5
alpha = 1
beta = 2
q = 1
best_path, best_distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
print("Best path:", best_path)
print("Best distance:", best_distance)