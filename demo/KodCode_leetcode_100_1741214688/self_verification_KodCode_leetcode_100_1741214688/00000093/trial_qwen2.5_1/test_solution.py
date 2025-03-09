from solution import *

import pytest

def test_longest_consecutive_positive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([10, 20, 30, 40]) == 1
    assert longest_consecutive([100, 90, 80, 70, 101, 102, 103]) == 3
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

def test_longest_consecutive_empty():
    assert longest_consecutive([]) == 0

def test_longest_consecutive_one_element():
    assert longest_consecutive([5]) == 1

def test_longest_consecutive_duplicate_elements():
    assert longest_consecutive([1, 2, 2, 3, 3, 4, 4, 5]) == 5

def test_longest_consecutive_sequence_not_consecutive():
    assert longest_consecutive([5, 6, 7, 2, 3, 4]) == 4
    assert longest_consecutive([10, 12, 13, 11]) == 3