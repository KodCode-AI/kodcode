from solution import *

def test_find_next_prime():
    assert find_next_prime(10) == 11
    assert find_next_prime(29) == 31
    assert find_next_prime(100) == 101
    assert find_next_prime(131) == 137
    assert find_next_prime(1) == 2
    assert find_next_prime(2) == 3
    assert find_next_prime(3) == 5

test_find_next_prime()