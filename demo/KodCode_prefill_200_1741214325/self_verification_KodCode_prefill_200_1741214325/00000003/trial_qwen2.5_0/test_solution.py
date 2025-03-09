from solution import *

import pytest
from solution import merge_sorted_lists
from heapq import merge as built_in_merge

def test_merge_sorted_lists_positive():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == list(built_in_merge([1, 3, 5], [2, 4, 6]))

def test_merge_empty_lists():
    assert merge_sorted_lists([], []) == []
    assert merge_sorted_lists([], [2, 4, 6]) == [2, 4, 6]
    assert merge_sorted_lists([1, 3, 5], []) == [1, 3, 5]

def test_merge_with_common_elements():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == list(built_in_merge([1, 3, 5], [2, 4, 6]))
    assert merge_sorted_lists([1, 3, 5], [5, 6]) == list(built_in_merge([1, 3, 5], [5, 6]))

def test_merge_mixed_sign_numbers():
    assert merge_sorted_lists([-1, 0, 2], [-2, -2, 3]) == list(built_in_merge([-1, 0, 2], [-2, -2, 3]))