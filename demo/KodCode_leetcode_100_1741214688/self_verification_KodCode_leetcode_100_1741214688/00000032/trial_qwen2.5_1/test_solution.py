from solution import *

import pytest

from solution import calculate_result

def test_calculate_result():
    assert calculate_result([1, 2, 3, 4, 5]) == [0, 1, 3, 6, 10]
    assert calculate_result([1, 1, 2, 2, 2, 3]) == [0, 0, 3, 6, 8, 9]
    assert calculate_result([10, 20, 30, 40, 50]) == [0, 0, 0, 0, 0]
    assert calculate_result([50, 40, 30, 20, 10]) == [0, 0, 0, 0, 0]
    assert calculate_result([1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0]
    assert calculate_result([5, 3, 4, 2, 1]) == [4, 3, 3, 2, 0]
    assert calculate_result([2, 2, 2, 2, 2, 2]) == [0, 0, 0, 0, 0, 0]

def test_edge_cases():
    assert calculate_result([1]) == [0]
    assert calculate_result([]) == []