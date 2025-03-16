from solution import *

from solution import is_prime

def test_is_prime_with_prime_number():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(11) == True

def test_is_prime_with_non_prime_number():
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(15) == False
    assert is_prime(100) == False

def test_is_prime_with_edge_cases():
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-3) == False
    assert is_prime(-1) == False