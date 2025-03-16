from solution import *

import pytest
from heapq import merge as test_merge
from solution import merge_sorted_lists

def test_merge_sorted_lists_positive():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

def test_merge_empty_lists():
    assert merge_sorted_lists([], []) == []

def test_merge_with_duplicates():
    assert merge_sorted_lists([1, 3, 3], [2, 3, 4]) == [1, 2, 3, 3, 3, 4]

def test_merge_mixed_signs():
    assert merge_sorted_lists([-2, 0, 2], [-3, 1, 3]) == [-3, -2, 0, 1, 2, 3]

def test_merge_with_same_elements():
    assert merge_sorted_lists([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]

def test_merge_with_different_lengths():
    assert merge_sorted_lists([1, 3, 5, 7], [2, 4, 6]) == [1, 2, 3, 4, 5, 6, 7]