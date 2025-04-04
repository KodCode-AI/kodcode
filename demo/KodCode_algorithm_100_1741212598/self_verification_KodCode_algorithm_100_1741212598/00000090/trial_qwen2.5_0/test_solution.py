from solution import *

import pytest

def test_calculate_difference():
    assert calculate_difference(10) == 2640
    assert calculate_difference(15) == 13160
    assert calculate_difference(20) == 41230
    assert calculate_difference(50) == 1582700
    assert calculate_difference(1) == 0
    assert calculate_difference(1000) == 25363260130

def test_edge_cases():
    assert calculate_difference(1) == 0
    assert calculate_difference(2) == 4
    assert calculate_difference(3) == 22
    assert calculate_difference(4) == 70
    assert calculate_difference(10**6) == 25333350000000

def test_large_n():
    assert calculate_difference(1000000) == 253333333333325000