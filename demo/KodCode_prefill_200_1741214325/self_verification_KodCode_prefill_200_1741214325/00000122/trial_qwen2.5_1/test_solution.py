from solution import *

from solution import find_max_recursive

def test_find_max_recursive_empty():
    assert find_max_recursive([]) == None

def test_find_max_recursive_positive():
    assert find_max_recursive([1, 5, 3, 9, 2]) == 9

def test_find_max_recursive_negative():
    assert find_max_recursive([-1, -5, -3, -9, -2]) == -1

def test_find_max_recursive_mixed():
    assert find_max_recursive([1, -5, 3, -9, 2]) == 3

def test_find_max_recursive_single_element():
    assert find_max_recursive([42]) == 42