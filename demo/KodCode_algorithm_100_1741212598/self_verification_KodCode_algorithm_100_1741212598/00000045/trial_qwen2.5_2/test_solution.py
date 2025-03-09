from solution import *

from solution import gcd_by_iterative, find_mod_inverse

def test_find_mod_inverse():
    assert find_mod_inverse(3, 11) == 4
    assert find_mod_inverse(17, 3120) == 2753
    assert find_mod_inverse(25, 18) == 11
    try:
        find_mod_inverse(10, 20)
    except ValueError as e:
        assert str(e) == "mod inverse of 10 and 20 does not exist"
    else:
        assert False, "ValueError not raised"

def test_gcd_by_iterative():
    assert gcd_by_iterative(3, 11) == 1
    assert gcd_by_iterative(17, 3120) == 1
    assert gcd_by_iterative(10, 20) == 10