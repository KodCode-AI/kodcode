from solution import *

import pytest

def test_find_next_power_of_two_zero():
    assert find_next_power_of_two(0) == 1

def test_find_next_power_of_two_one():
    assert find_next_power_of_two(1) == 2

def test_find_next_power_of_two_five():
    assert find_next_power_of_two(5) == 8

def test_find_next_power_of_two_sixteen():
    assert find_next_power_of_two(16) == 32

def test_find_next_power_of_two_twenty_three():
    assert find_next_power_of_two(23) == 32

def test_find_next_power_of_two_three():
    assert find_next_power_of_two(3) == 4

def test_find_next_power_of_two_larger_numbers():
    assert find_next_power_of_two(1023) == 1024
    assert find_next_power_of_two(1024) == 2048
    assert find_next_power_of_two(2047) == 2048