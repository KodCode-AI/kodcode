from solution import *

from solution import findMaxLength

def test_findMaxLength():
    assert findMaxLength([0, 1]) == 2
    assert findMaxLength([0, 1, 0]) == 2
    assert findMaxLength([0, 1, 0, 1]) == 4
    assert findMaxLength([0, 0, 1, 0, 1, 1, 0, 1]) == 7
    assert findMaxLength([1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]) == 10

def test_empty_input():
    assert findMaxLength([]) == 0

def test_single_element():
    assert findMaxLength([0]) == 0
    assert findMaxLength([1]) == 0

def test_all_zeros():
    assert findMaxLength([0, 0, 0, 0]) == 0

def test_all_ones():
    assert findMaxLength([1, 1, 1, 1]) == 0

def test_mismatched_lengths():
    assert findMaxLength([0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1]) == 8