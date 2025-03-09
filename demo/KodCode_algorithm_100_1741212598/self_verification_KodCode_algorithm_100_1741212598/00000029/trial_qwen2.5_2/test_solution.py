from solution import *

import pytest
from math import isclose

def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def property_check(p: int) -> bool:
    n = 1
    while n**3 < (n**3 + n**2 * p):
        if isclose((n**3 + n**2 * p)**(1/3), int((n**3 + n**2 * p)**(1/3))):
            return True
        n += 1
    return False

def test_check_primes_with_property():
    assert check_primes_with_property(100) == 4
    assert check_primes_with_property(1000) == 10
    assert check_primes_with_property(10000) == 12
    assert check_primes_with_property(100000) == 13
    assert check_primes_with_property(1000000) == 15

def test_property_check():
    assert property_check(2) is True
    assert property_check(3) is True
    assert property_check(5) is False
    assert property_check(7) is False
    assert property_check(11) is True

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(29) is True
    assert is_prime(30) is False
    assert is_prime(97) is True