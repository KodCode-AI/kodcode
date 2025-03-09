from solution import *

from solution import gcd

def test_gcd_positive_numbers():
    assert gcd(48, 18) == 6

def test_gcd_with_zero():
    assert gcd(0, 5) == 5
    assert gcd(0, 0) == 0

def test_gcd_negative_numbers():
    assert gcd(-25, 10) == 5
    assert gcd(-15, -10) == 5

def test_gcd_mixed_sign_numbers():
    assert gcd(-20, 15) == 5
    assert gcd(20, -15) == 5

def test_gcd_large_numbers():
    assert gcd(123456, 56789) == 1