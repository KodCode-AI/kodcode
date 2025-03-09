from solution import *

from solution import is_prime

def test_is_prime_with_primes():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

def test_is_prime_with_non_primes():
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_is_prime_edge_cases():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(-3) == False

def test_is_prime_large_numbers():
    assert is_prime(9973) == True
    assert is_prime(9975) == False
    assert is_prime(9991) == True
    assert is_prime(9999) == False