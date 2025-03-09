from solution import *

import heapq
from solution import merge_sorted_lists

def test_merge_sorted_lists_with_two_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_lists_with_duplicates():
    assert merge_sorted_lists([1, 3, 5, 5], [2, 4, 6, 6]) == [1, 2, 3, 4, 5, 5, 6, 6]

def test_merge_sorted_lists_with_unsorted_lists():
    assert merge_sorted_lists([3, 1, 5], [6, 4, 2]) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_lists_with_empty_lists():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_lists([], []) == []