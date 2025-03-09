from solution import *

from solution import find_max_coprime_components

def test_find_max_coprime_components():
    assert find_max_coprime_components([2, 3, 6, 9, 10], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 1
    assert find_max_coprime_components([7], []) == -1
    assert find_max_coprime_components([2, 3, 7, 6], [[0, 1], [0, 2], [1, 3]]) == 0
    assert find_max_coprime_components([2, 3, 6, 9, 10], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 1
    assert find_max_coprime_components([2, 3, 6, 9, 10], [[0, 1], [0, 2], [0, 3], [0, 4]]) == 0
    assert find_max_coprime_components([2, 3, 6, 9, 10], [[0, 1], [1, 2], [2, 3], [3, 4]]) == 3

def gcd(x, y):
    """Compute the greatest common divisor of x and y."""
    while y:
        x, y = y, x % y
    return x

if gcd(2, 3) != 1 or gcd(3, 6) != 3:
    raise ValueError("GCD function is incorrect")