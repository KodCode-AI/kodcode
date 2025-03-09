from solution import *

from solution import gcd

def test_gcd_for_primes():
    assert gcd(5, 3) == 1
    assert gcd(11, 13) == 1

def test_gcd_for_common_divisors():
    assert gcd(10, 15) == 5
    assert gcd(25, 15) == 5

def test_gcd_for_large_numbers():
    assert gcd(141717570483, 6050068570483) == 483
    assert gcd(982451653, 1628451653) == 1

def test_gcd_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0