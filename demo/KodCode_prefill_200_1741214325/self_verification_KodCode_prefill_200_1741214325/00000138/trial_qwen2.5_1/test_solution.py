from solution import *

from solution import findMaxLength

def test_findMaxLength_with_single_element_subarray():
    assert findMaxLength([0, 1]) == 2

def test_findMaxLength_with_mixed_sequence():
    assert findMaxLength([0, 1, 0, 1, 0, 1, 0]) == 7

def test_findMaxLength_with_all_zeros():
    assert findMaxLength([0, 0, 0, 0]) == 0

def test_findMaxLength_with_all_ones():
    assert findMaxLength([1, 1, 1, 1]) == 0

def test_findMaxLength_with_alternating_sequence():
    assert findMaxLength([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 10

def test_findMaxLength_with_reversed_alternating_sequence():
    assert findMaxLength([0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 10