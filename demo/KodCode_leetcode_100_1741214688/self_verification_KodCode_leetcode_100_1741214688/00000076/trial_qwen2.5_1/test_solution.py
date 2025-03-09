from solution import *

from solution import is_prime, digit_sum, count_prime_digit_sums

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(29) == True
    assert is_prime(25) == False

def test_digit_sum():
    assert digit_sum(123) == 6
    assert digit_sum(456) == 15
    assert digit_sum(789) == 24

def test_count_prime_digit_sums():
    assert count_prime_digit_sums(5) == 2  # 2, 3
    assert count_prime_digit_sums(10) == 4  # 2, 3, 5, 7
    assert count_prime_digit_sums(15) == 6  # 2, 3, 5, 7, 11, 13
    assert count_prime_digit_sums(22) == 8  # 2, 3, 5, 7, 11, 13, 17, 19