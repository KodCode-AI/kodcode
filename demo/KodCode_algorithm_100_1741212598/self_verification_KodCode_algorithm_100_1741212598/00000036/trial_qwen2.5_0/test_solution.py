from solution import *

import pytest
from solution import main, nearest_city_index, distances_sum

def test_main():
    cities = {
        0: [0, 0],
        1: [0, 5],
        2: [3, 8],
        3: [8, 10],
        4: [12, 14]
    }
    ants_num = 10
    iterations_num = 10
    pheromone_evaporation = 0.5
    alpha = 2
    beta = 5
    q = 100
    
    path, distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
    assert len(path) == 5 and path[0] == 0 and path[4] == 0
    assert distance > 0

def test_main_single_city():
    cities = {
        0: [0, 0]
    }
    ants_num = 10
    iterations_num = 10
    pheromone_evaporation = 0.5
    alpha = 2
    beta = 5
    q = 100
    
    path, distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
    assert len(path) == 1 and path[0] == 0
    assert distance == 0

def test_main_empty_city():
    cities = {}
    ants_num = 10
    iterations_num = 10
    pheromone_evaporation = 0.5
    alpha = 2
    beta = 5
    q = 100
    
    path, distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
    assert path == [] and distance == 0

def test_nearest_city_index():
    current_city = 0
    unvisited_cities = [1, 2, 3, 4]
    pheromone = {0: {1: 1, 2: 2, 3: 3, 4: 4}, 1: {0: 1, 2: 2, 3: 3, 4: 4}, 2: {0: 1, 1: 2, 3: 3, 4: 4}, 3: {0: 1, 1: 2, 2: 3, 4: 4}, 4: {0: 1, 1: 2, 2: 3, 3: 4}}
    alpha = 2
    beta = 5
    cities = {
        0: [0, 0],
        1: [0, 5],
        2: [3, 8],
        3: [8, 10],
        4: [12, 14]
    }
    
    index = nearest_city_index(current_city, unvisited_cities, pheromone, alpha, beta, cities)
    assert index in [1, 2, 3, 4]

def test_distances_sum():
    cities = {
        0: [0, 0],
        1: [0, 5],
        2: [3, 8],
        3: [8, 10],
        4: [12, 14]
    }
    
    distances = distances_sum(cities)
    assert distances[(0, 1)] == 5
    assert distances[(0, 2)] == 8.06225774829855
    assert distances[(1, 2)] == 5
    assert distances[(0, 3)] == 10
    assert distances[(1, 3)] == 5