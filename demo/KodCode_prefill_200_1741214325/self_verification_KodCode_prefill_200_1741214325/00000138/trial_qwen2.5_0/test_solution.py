from solution import *

from solution import findMaxLength

def test_findMaxLength_empty_array():
    assert findMaxLength([]) == 0

def test_findMaxLength_single_zero():
    assert findMaxLength([0]) == 0

def test_findMaxLength_single_one():
    assert findMaxLength([1]) == 0

def test_findMaxLength_equal_zeros_and_ones():
    assert findMaxLength([0, 1]) == 2
    assert findMaxLength([1, 0]) == 2

def test_findMaxLength_longest_subarray():
    assert findMaxLength([0, 1, 0, 1, 0]) == 4

def test_findMaxLength_mixed_sequence():
    assert findMaxLength([1, 0, 1, 1, 0, 0, 1]) == 7