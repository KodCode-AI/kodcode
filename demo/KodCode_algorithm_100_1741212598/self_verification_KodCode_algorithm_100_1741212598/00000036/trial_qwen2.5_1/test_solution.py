from solution import *

import pytest
from solution import main

def test_empty_city_list():
    cities = {}
    ants_num = 1
    iterations_num = 1
    pheromone_evaporation = 0.5
    alpha = 1
    beta = 2
    q = 1
    best_path, best_distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
    assert best_path == []

def test_single_city():
    cities = {0: [0, 0]}
    ants_num = 1
    iterations_num = 1
    pheromone_evaporation = 0.5
    alpha = 1
    beta = 2
    q = 1
    best_path, best_distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
    assert best_path == [0]

def test_small_cities():
    cities = {
        0: [0, 0],
        1: [0, 5],
        2: [3, 8],
        3: [8, 10],
        4: [12, 12]
    }
    ants_num = 2
    iterations_num = 3
    pheromone_evaporation = 0.5
    alpha = 1
    beta = 2
    q = 1
    best_path, best_distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
    assert len(best_path) == 5 and best_path[0] == 0 and best_path[-1] == 0

def test_large_cities():
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
    ants_num = 5
    iterations_num = 50
    pheromone_evaporation = 0.5
    alpha = 1
    beta = 2
    q = 1
    best_path, best_distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
    assert len(best_path) == 8 and best_path[0] == 0 and best_path[-1] == 0

def test_random_cities():
    np.random.seed(42)
    cities = {i: [np.random.rand() * 20, np.random.rand() * 20] for i in range(10)}
    ants_num = 10
    iterations_num = 100
    pheromone_evaporation = 0.5
    alpha = 1
    beta = 2
    q = 1
    best_path, best_distance = main(cities, ants_num, iterations_num, pheromone_evaporation, alpha, beta, q)
    assert len(best_path) == 10 and best_path[0] == 0 and best_path[-1] == 0