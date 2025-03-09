from solution import *

from solution import is_prime, digit_sum, count_prime_digit_sum

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(11) == True
    assert is_prime(12) == False

def test_digit_sum():
    assert digit_sum(123) == 6
    assert digit_sum(4321) == 10
    assert digit_sum(8) == 8

def test_count_prime_digit_sum():
    assert count_prime_digit_sum(10) == 2  # 2 and 3
    assert count_prime_digit_sum(5) == 2  # 2 and 3
    assert count_prime_digit_sum(9) == 4  # 2, 3, 5, 7
    assert count_prime_digit_sum(31) == 12  # All numbers with prime digit sums up to 31