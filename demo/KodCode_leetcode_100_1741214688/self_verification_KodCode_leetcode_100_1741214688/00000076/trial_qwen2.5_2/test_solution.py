from solution import *

from solution import count_prime_digit_sums, is_prime, digit_sum

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(11) is True
    assert is_prime(12) is False

def test_digit_sum():
    assert digit_sum(123) == 6
    assert digit_sum(456) == 15
    assert digit_sum(789) == 24
    assert digit_sum(100) == 1

def test_count_prime_digit_sums():
    assert count_prime_digit_sums(10) == 2  # 2, 3
    assert count_prime_digit_sums(20) == 4  # 2, 3, 5, 7
    assert count_prime_digit_sums(30) == 5  # 2, 3, 5, 7, 11
    assert count_prime_digit_sums(100) == 25

# Additional edge cases
assert count_prime_digit_sums(1) == 1  # Only 2
assert count_prime_digit_sums(2) == 2  # 2, 3
assert count_prime_digit_sums(3) == 3  # 2, 3
assert count_prime_digit_sums(0) == 0  # No numbers to check