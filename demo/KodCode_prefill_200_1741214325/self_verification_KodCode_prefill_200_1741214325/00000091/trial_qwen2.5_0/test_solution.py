from solution import *

from solution import is_prime, find_primes_in_range

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(29) == True
    assert is_prime(30) == False

def test_find_primes_in_range():
    assert find_primes_in_range(5, 15) == [5, 7, 11, 13]
    assert find_primes_in_range(1, 10) == [2, 3, 5, 7]
    assert find_primes_in_range(20, 22) == []
    assert find_primes_in_range(14, 14) == []
    assert find_primes_in_range(11, 11) == [11]
    assert find_primes_in_range(10, 20) == [11, 13, 17, 19]

def test_find_primes_in_range_edge_cases():
    assert find_primes_in_range(0, 5) == [2, 3, 5]
    assert find_primes_in_range(5, 0) == []
    assert find_primes_in_range(0, 0) == []