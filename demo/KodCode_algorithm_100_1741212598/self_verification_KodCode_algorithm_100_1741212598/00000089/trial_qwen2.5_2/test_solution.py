from solution import *

import pytest

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(29) == True
    assert is_prime(33) == False
    assert is_prime(97) == True

def test_find_next_prime():
    assert find_next_prime(10) == 11
    assert find_next_prime(29) == 31
    assert find_next_prime(100) == 101
    assert find_next_prime(101) == 103
    assert find_next_prime(543) == 547
    assert find_next_prime(1000) == 1009
    assert find_next_prime(999983) == 999991
    assert find_next_prime(1000000) == 1000003

pytest.main()