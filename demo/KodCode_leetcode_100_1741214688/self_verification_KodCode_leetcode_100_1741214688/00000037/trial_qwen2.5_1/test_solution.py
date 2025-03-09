from solution import *

from solution import min_intervals_to_remove

def test_no_intervals():
    assert min_intervals_to_remove([]) == 0

def test_one_interval():
    assert min_intervals_to_remove([[1, 2]]) == 0

def test_separate_intervals():
    assert min_intervals_to_remove([[1, 3], [6, 9], [2, 5]]) == 0

def test_overlapping_intervals_by_end():
    assert min_intervals_to_remove([[1, 2], [2, 3], [3, 4]]) == 0

def test_several_overlapping_intervals():
    assert min_intervals_to_remove([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2

def test_single_overlapping_with_one():
    assert min_intervals_to_remove([[1, 3], [2, 4]]) == 1

def test_multiple_overlaps():
    assert min_intervals_to_remove([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2