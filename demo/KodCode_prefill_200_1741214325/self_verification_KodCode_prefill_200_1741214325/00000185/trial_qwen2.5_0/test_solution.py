from solution import *

from solution import gcd, lcm

def test_gcd():
    assert gcd(3, 5) == 1
    assert gcd(25, 15) == 5
    assert gcd(100, 200) == 100

def test_lcm():
    assert lcm(3, 5) == 15
    assert lcm(25, 15) == 75
    assert lcm(100, 200) == 200

def test_lcm_with_gcd():
    assert lcm(2, 3) == 6  # LCM using gcd should match the direct calculation
    assert lcm(12, 15) == 60
    assert lcm(7, 14) == 14