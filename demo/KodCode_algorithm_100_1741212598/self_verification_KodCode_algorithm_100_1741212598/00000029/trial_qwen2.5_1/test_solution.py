from solution import *

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(16) == False

def test_is_cube():
    assert is_cube(1) == True
    assert is_cube(8) == True
    assert is_cube(27) == True
    assert is_cube(64) == True
    assert is_cube(5) == False

def test_check_primes_with_property():
    assert check_primes_with_property(100) == 4
    assert check_primes_with_property(1000) == 10
    assert check_primes_with_property(10000) == 12
    assert check_primes_with_property(100000) == 13
    assert check_primes_with_property(1000000) == 15

from solution import check_primes_with_property