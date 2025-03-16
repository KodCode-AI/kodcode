from solution import *

from solution import binary_search

def test_binary_search_positive():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([10, 20, 30, 40, 50], 40) == 3

def test_binary_search_not_found():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([10, 20, 30, 40, 50], 7) == -1

def test_binary_search_single_element():
    assert binary_search([5], 5) == 0
    assert binary_search([5], 4) == -1

def test_binary_search_empty_list():
    assert binary_search([], 1) == -1
    assert binary_search([], 2) == -1

def test_binary_search_edge_cases():
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 0
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 9