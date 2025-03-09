from solution import *

``
from solution import gcd, lcm, smallest_multiple

def test_gcd():
    assert gcd(8, 12) == 4
    assert gcd(17, 13) == 1

def test_lcm():
    assert lcm(8, 12) == 24
    assert lcm(17, 13) == 221

def test_smallest_multiple():
    assert smallest_multiple(10, 15) == 30
    assert smallest_multiple(7, 5) == 35
    assert smallest_multiple(21, 6) == 42
    assert smallest_multiple(15, 17) == 255

def test_smallest_multiple_with_gcd():
    assert smallest_multiple(10, 15) == lcm(10, 15)