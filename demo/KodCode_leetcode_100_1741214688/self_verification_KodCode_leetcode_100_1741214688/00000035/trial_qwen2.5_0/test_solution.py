from solution import *

def test_maximize_gcd():
    assert maximize_gcd([2, 3, 6], 1) == 4
    assert maximize_gcd([3, 9, 6], 2) == 3
    assert maximize_gcd([3, 9, 6], 3) == 9
    assert maximize_gcd([2, 4, 6, 8], 10) == 2
    assert maximize_gcd([10, 10, 10, 10], 5) == 10
    assert maximize_gcd([1, 3, 5, 7], 2) == 1