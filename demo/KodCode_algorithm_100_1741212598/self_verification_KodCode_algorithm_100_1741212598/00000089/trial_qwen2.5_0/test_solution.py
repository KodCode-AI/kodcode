from solution import *

from solution import find_next_prime, is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True

def test_find_next_prime():
    assert find_next_prime(10) == 11
    assert find_next_prime(29) == 31
    assert find_next_prime(100) == 101
    assert find_next_prime(53) == 59
    assert find_next_prime(200) == 211