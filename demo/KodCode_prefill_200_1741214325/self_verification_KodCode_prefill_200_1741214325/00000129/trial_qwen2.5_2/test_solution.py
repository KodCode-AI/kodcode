from solution import *

from solution import gcd

def test_gcd_positive_numbers():
    assert gcd(12, 16) == 4

def test_gcd_when_one_number_is_multiple_of_other():
    assert gcd(50, 20) == 10

def test_gcd_of_primes():
    assert gcd(17, 23) == 1

def test_gcd_with_zero():
    assert gcd(12, 0) == 12
    assert gcd(0, 12) == 12
    assert gcd(0, 0) == 0

def test_gcd_with_negative_numbers():
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6