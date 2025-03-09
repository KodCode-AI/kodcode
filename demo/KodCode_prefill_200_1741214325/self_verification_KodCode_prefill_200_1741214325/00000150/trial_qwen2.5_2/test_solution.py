from solution import *

import pytest

def test_is_power_of_two_positive():
    assert is_power_of_two(1) is True
    assert is_power_of_two(2) is True
    assert is_power_of_two(4) is True
    assert is_power_of_two(16) is True

def test_is_power_of_two_not_positive():
    assert is_power_of_two(0) is False
    assert is_power_of_two(-2) is False
    assert is_power_of_two(-4) is False

def test_is_power_of_two_large_values():
    assert is_power_of_two(1048576) is True  # 2^20
    assert is_power_of_two(2097152) is False  # 2^21 - 1 is not a power of two

def test_is_power_of_two_edge_cases():
    assert is_power_of_two(3) is False
    assert is_power_of_two(8) is True
    assert is_power_of_two(1023) is False  # 2^10 - 1 is not a power of two