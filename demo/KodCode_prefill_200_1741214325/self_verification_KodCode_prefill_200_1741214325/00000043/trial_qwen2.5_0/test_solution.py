from solution import *

from solution import longest_increasing_subsequence

def test_lis_empty():
    assert longest_increasing_subsequence([]) == 0

def test_lis_single_element():
    assert longest_increasing_subsequence([1]) == 1

def test_lis_constant_elements():
    assert longest_increasing_subsequence([1, 1, 1, 1]) == 1

def test_lis_increasing_sequence():
    assert longest_increasing_subsequence([1, 2, 3]) == 3

def test_lis_decreasing_sequence():
    assert longest_increasing_subsequence([3, 2, 1]) == 1

def test_lis_random_sequence():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_lis_with_repeated_elements():
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4