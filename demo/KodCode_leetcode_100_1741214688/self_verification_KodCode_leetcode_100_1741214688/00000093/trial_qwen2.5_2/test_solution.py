from solution import *

import pytest
from solution import longest_consecutive

def test_longest_consecutive_empty_list():
    assert longest_consecutive([]) == 0

def test_longest_consecutive_no_sequence():
    assert longest_consecutive([204, 205, 206, 208, 209]) == 0

def test_longest_consecutive_single_sequence():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([103, 104, 105, 102]) == 3

def test_longest_consecutive_multiple_sequences():
    assert longest_consecutive([1, 9, 3, 10, 4, 20, 2]) == 4
    assert longest_consecutive([101, 102, 104, 106, 6, 7, 8, 9, 103, 105]) == 5

def test_longest_consecutive_all_same_number():
    assert longest_consecutive([5, 5, 5, 5]) == 1