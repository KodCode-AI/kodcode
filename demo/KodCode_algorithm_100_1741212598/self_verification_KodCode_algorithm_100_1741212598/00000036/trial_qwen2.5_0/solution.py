import random
from math import sqrt
from collections import defaultdict

def distance(city1, city2):
    """
    Returns the Euclidean distance between two cities.
    """
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q):
    """
    Implements the Ant Colony Optimization (ACO) algorithm for the Traveling Salesman Problem (TSP).
    """
    cities_num = len(cities)
    if cities_num == 0: return ([], 0)
    if cities_num == 1: return ([0], 0)
    
    # Initialize pheromone matrix
    pheromone = defaultdict(lambda: defaultdict(lambda: 1 / (cities_num ** 2)))
    
    # Initialize best path and its distance
    best_path = None
    best_distance = float('inf')
    
    for _ in range(iterations_num):
        for _ in range(ants_num):
            ant_path = []
            unvisited_cities = list(range(1, cities_num))
            current_city = 0
            ant_path.append(0)
            
            while unvisited_cities:
                next_city_idx = nearest_city_index(current_city, unvisited_cities, pheromone, alpha, beta, cities)
                ant_path.append(next_city_idx)
                pheromone[current_city][next_city_idx] += 1 / distances_sum[current_city][next_city_idx]
                unvisited_cities.remove(next_city_idx)
                current_city = next_city_idx
            
            ant_path.append(0)
            ant_distance = sum(distance(cities[path_idx], cities[path_idx + 1]) for path_idx in ant_path)
            if ant_distance < best_distance:
                best_path = ant_path.copy()
                best_distance = ant_distance
            
            # Update pheromones after each ant's path
            for i in range(cities_num + 1):
                for j in range(cities_num + 1):
                    pheromone[i][j] *= (1 - pheromone_evaporation)
                    if (i, j) in [(path[i], path[i + 1]) for path in [best_path]]:
                        pheromone[i][j] += (alpha * q) / best_distance
            
            distances_sum = defaultdict(lambda: defaultdict(lambda: 0))
            for path in [best_path]:
                for i in range(cities_num + 1):
                    for j in range(i + 1, cities_num + 1):
                        distances_sum[path[i]][path[j]] += distance(cities[path[i]], cities[path[j]])
    
    return best_path, best_distance

def nearest_city_index(current_city, unvisited_cities, pheromone, alpha, beta, cities):
    probabilities = []
    for city in unvisited_cities:
        try:
            denominator = 1 / (pheromone[current_city][city] ** alpha * distance(cities[current_city], cities[city]) ** beta)
            probabilities.append(denominator)
        except ZeroDivisionError:
            probabilities.append(0)
    
    # Normalize probabilities
    sum_probabilities = sum(probabilities)
    normalized_probabilities = [prob / sum_probabilities for prob in probabilities]
    
    # Choose next city randomly based on probabilities
    next_city_idx = random.choices(unvisited_cities, weights=normalized_probabilities)[0]
    
    return next_city_idx

def distances_sum(cities):
    distances = {}
    for i, city1 in cities.items():
        for j, city2 in cities.items():
            if i < j:
                distances[(i, j)] = distance(city1, city2)
    return distances