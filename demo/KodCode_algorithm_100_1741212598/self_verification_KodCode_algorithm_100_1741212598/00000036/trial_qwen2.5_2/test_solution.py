from solution import *

import pytest
import itertools

def prepare_cities(num_cities):
    """Prepare a list of cities with random coordinates."""
    return {i: [random.uniform(0, 20), random.uniform(0, 20)] for i in range(num_cities)}

def check_route_distance(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(cities[route[i]], cities[route[i + 1]])
    total_distance += calculate_distance(cities[route[-1]], cities[route[0]])
    return total_distance

def test_main_no_cities():
    assert main([], 5, 10, 0.5, 1, 1, 10) == ([], float('inf'))

def test_main_single_city():
    cities = prepare_cities(1)
    result = main(cities, 5, 10, 0.5, 1, 1, 1)
    assert len(result[0]) == 1

def test_main_small_population():
    cities = prepare_cities(10)
    result = main(cities, 5, 10, 0.5, 1, 1, 1)
    assert result[1] > 0, "Distance should be greater than 0"

def test_main_large_population():
    cities = prepare_cities(50)
    result = main(cities, 100, 100, 0.5, 1, 1, 1)
    assert result[1] > 0, "Distance should be greater than 0"
    assert result[0] == list(range(50)), "No optimization is expected in this test"

def test_main_consistency():
    cities = prepare_cities(5)
    routes = []
    for _ in range(10):
        result = main(cities, 5, 10, 0.5, 1, 1, 1)
        routes.append((result[0], result[1]))
    previous_distance = float('inf')
    for route, distance in routes:
        assert distance <= previous_distance, "Distance should not increase in consecutive runs"
        previous_distance = distance