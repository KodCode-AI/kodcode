from solution import *

def test_find_primes_in_range():
    assert find_primes_in_range(5, 11) == [5, 7, 11]
    assert find_primes_in_range(14, 19) == [17, 19]
    assert find_primes_in_range(22, 29) == [23, 29]
    assert find_primes_in_range(1, 3) == [2, 3]
    assert find_primes_in_range(100, 104) == []
    assert find_primes_in_range(75, 80) == [79]