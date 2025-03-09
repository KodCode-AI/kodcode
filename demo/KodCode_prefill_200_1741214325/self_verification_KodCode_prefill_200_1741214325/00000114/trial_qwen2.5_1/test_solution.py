from solution import *

from solution import is_prime

def test_is_prime_two():
    assert is_prime(2) == True

def test_is_prime_three():
    assert is_prime(3) == True

def test_is_prime_four():
    assert is_prime(4) == False

def test_is_prime_negative_number():
    assert is_prime(-7) == False

def test_is_prime_large_number():
    assert is_prime(11227278127) == True

def test_is_prime_seven():
    assert is_prime(7) == True

def test_is_prime_eight_to_fifteen():
    for i in range(8, 16):
        assert is_prime(i) == False

def test_is_prime_big_prime():
    assert is_prime(2999999937) == True

def test_is_prime_non_prime():
    assert is_prime(15) == False