from solution import *

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1, 3, 5], 3) == 1
    assert binary_search([1, 3, 5], 2) == -1
    assert binary_search([1, 2, 3, 4, 5, 5, 6], 5) == 4  # Duplicate values in the list
    assert binary_search([1, 2, 3, 4, 5], -1) == -1  # Target not in the list
    assert binary_search([10, 20, 30, 40, 50], 30) == 2  # Middle element
    assert binary_search([10, 20, 30, 40, 50], 25) == -1  # Element not found in the middle range