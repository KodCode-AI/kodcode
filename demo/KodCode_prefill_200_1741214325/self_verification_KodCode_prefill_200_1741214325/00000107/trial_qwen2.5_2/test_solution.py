from solution import *

from solution import find_pairs

def test_find_pairs_with_positive_numbers():
    assert find_pairs([1, 2, 3, 4, 5], 7) == [(2, 5), (3, 4)]

def test_find_pairs_with_negative_and_positive_numbers():
    assert find_pairs([-1, 1, -2, 2, 3], 0) == [(-1, 1), (-2, 2)]

def test_find_pairs_with_no_pairs():
    assert find_pairs([1, 3, 5, 7], 12) == []

def test_find_pairs_single_element():
    assert find_pairs([5], 5) == []

def test_find_pairs_duplicate_pairs():
    assert find_pairs([1, 2, 2, 4, 5], 7) == [(2, 5), (2, 5)]