from solution import *

from solution import longest_consecutive

def test_longest_consecutive_empty():
    assert longest_consecutive([]) == 0

def test_longest_consecutive_single_element():
    assert longest_consecutive([1]) == 1

def test_longest_consecutive_no_sequence():
    assert longest_consecutive([5, 2, 4, 1, 3]) == 5  # No sequence, but sorted elements

def test_longest_consecutive_with_sequence():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # Longest sequence [1, 2, 3, 4]
    assert longest_consecutive([10, 5, 12, 3]) == 2  # Longest sequence [3, 5]
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9  # Longest sequence [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert longest_consecutive([100, 4, 200, 1, 3, 2, 400, 401]) == 4  # Longest sequence [1, 2, 3, 4]