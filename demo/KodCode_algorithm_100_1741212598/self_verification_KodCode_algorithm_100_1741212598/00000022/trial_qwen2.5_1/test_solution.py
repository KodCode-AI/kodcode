from solution import *

``
import pytest

def test_find_weird_numbers():
    assert find_weird_numbers([69, 70, 71]) == [70]
    assert find_weird_numbers([12, 18, 20, 24, 25]) == [20, 24]
    assert find_weird_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []
    assert find_weird_numbers([70, 8316, 1004, 23190, 28079825]) == [8316, 2016, 2574, 23190, 28079825]
    assert find_weird_numbers([1560]) == [1560]