from solution import *

from solution import binary_search

def test_binary_search_found():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 4) == 3
    assert binary_search([-5, -3, 0, 3, 7, 8, 9], 7) == 5
    assert binary_search([10, 20, 30, 40, 50], 30) == 2

def test_binary_search_not_found():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([-5, -3, 0, 3, 7, 8, 9], 4) == -1
    assert binary_search([1, 3, 5, 7], 2) == -1

def test_binary_search_empty_list():
    assert binary_search([], 1) == -1