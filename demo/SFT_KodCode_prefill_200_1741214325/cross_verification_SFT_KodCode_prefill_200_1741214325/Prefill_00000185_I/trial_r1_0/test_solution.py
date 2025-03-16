from solution import *

from solution import gcd, lcm

def test_gcd():
    assert gcd(12, 18) == 6
    assert gcd(7, 13) == 1
    assert gcd(98, 56) == 14

def test_lcm():
    assert lcm(12, 18) == 36
    assert lcm(7, 13) == 91
    assert lcm(98, 56) == 392

def test_lcm_with_gcd():
    # LCM * GCD = |a*b|
    a, b = 30, 45
    assert lcm(a, b) * gcd(a, b) == abs(a * b)