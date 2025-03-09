from solution import *

from solution import sumOfMaxElements

def test_sumOfMaxElements():
    assert sumOfMaxElements([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 18
    assert sumOfMaxElements([[10, -2, 3], [3, 5, 7], [-1, -5, -10]]) == 15
    assert sumOfMaxElements([[0]]) == 0
    assert sumOfMaxElements([[5, 5, 5], [5, 5, 5]]) == 10
    assert sumOfMaxElements([[1000, -1000, 1000], [-1000, 1000, -1000]]) == 2000