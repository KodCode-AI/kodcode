from solution import *

from solution import max_possible_gcd

def test_max_possible_gcd():
    assert max_possible_gcd([2, 6, 3, 4], 1) == 6
    assert max_possible_gcd([3, 9, 5], 2) == 3
    assert max_possible_gcd([1, 2, 3, 6], 3) == 6
    assert max_possible_gcd([10, 10], 0) == 10
    assert max_possible_gcd([4, 8, 16], 1) == 8
    assert max_possible_gcd([1, 2, 3], 3) == 1

# Test case with a larger k value
    assert max_possible_gcd([2, 4, 8], 5) == 16