from solution import *

import pytest

def test_find_mod_inverse():
    assert find_mod_inverse(3, 11) == 4
    assert find_mod_inverse(17, 3120) == 2753
    with pytest.raises(ValueError):
        find_mod_inverse(10, 20)
    with pytest.raises(ValueError):
        find_mod_inverse(25, 100)

def test_mod_inverse.mul_behavior():
    a = 3
    m = 11
    inv = find_mod_inverse(a, m)
    assert (a * inv) % m == 1

def test_gcd_aliasing():
    assert gcd_by_iterative(3, 11) == 1
    assert gcd_by_iterative(17, 3120) == 1
    assert gcd_by_iterative(10, 20) == 10