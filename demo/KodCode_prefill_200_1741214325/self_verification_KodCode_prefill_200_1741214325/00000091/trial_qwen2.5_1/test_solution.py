from solution import *

from solution import find_primes_in_range

def test_find_primes_in_range():
    assert find_primes_in_range(5, 10) == [5, 7]
    assert find_primes_in_range(10, 15) == [11, 13]
    assert find_primes_in_range(20, 25) == [23]
    assert find_primes_in_range(1, 5) == [2, 3, 5]
    assert find_primes_in_range(14, 14) == []
    assert find_primes_in_range(30, 40) == [31, 37]
    assert find_primes_in_range(50, 60) == [53, 59]