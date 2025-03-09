from solution import *

from solution import sumOfMaxElements

def test_sumOfMaxElements():
    assert sumOfMaxElements([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 18
    assert sumOfMaxElements([[10], [20], [30]]) == 60
    assert sumOfMaxElements([[0, -1, -2], [-3, -4, -5], [-6, -7, -8]]) == -3
    assert sumOfMaxElements([[5, 5, 5], [5, 5, 5], [5, 5, 5]]) == 15
    assert sumOfMaxElements([[1, 2], [3, 4], [5, 6], [7, 8]]) == 26

def test_with_single_row_matrix():
    assert sumOfMaxElements([[1, 2, 3, 4, 5]]) == 5
    assert sumOfMaxElements([[100]]) == 100

def test_with_empty_matrix():
    assert sumOfMaxElements([]) == 0
    assert sumOfMaxElements([[]]) == 0