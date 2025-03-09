from solution import *

import pytest
from solution import assign_values

def test_simple_case():
    assert assign_values(4, [[0, 1], [1, 2], [2, 0], [1, 3]]) == 8

def test_random_case():
    assert assign_values(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 1]]) == 13

def test_single_city():
    assert assign_values(1, []) == 1

def test_two_cities():
    assert assign_values(2, [[0, 1]]) == 3

def test_three_cities():
    assert assign_values(3, [[0, 1], [1, 2], [2, 0]]) == 6

def test_four_cities():
    assert assign_values(4, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 0], [2, 3]]) == 12