from solution import *

import pytest

def test_divisors_sum():
    assert divisors_sum(12) == 16  # 1 + 2 + 3 + 4 + 6
    assert divisors_sum(28) == 28  # 1 + 2 + 4 + 7 + 14
    
def test_is_weird_number():
    assert is_weird_number(70) is True
    assert is_weird_number(20) is True
    assert is_weird_number(24) is True
    assert is_weird_number(71) is False
    assert is_weird_number(1) is False
    assert is_weird_number(12) is False

def test_find_weird_numbers():
    assert find_weird_numbers([69, 70, 71]) == [70]
    assert find_weird_numbers([12, 18, 20, 24, 25]) == [20, 24]
    assert find_weird_numbers([1, 2, 3, 4, 5, 71]) == []