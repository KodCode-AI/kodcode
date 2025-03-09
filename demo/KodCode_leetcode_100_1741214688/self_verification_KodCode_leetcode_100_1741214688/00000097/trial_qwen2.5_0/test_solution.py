from solution import *

from solution import sumOfMaxElements

def test_sumOfMaxElements():
    assert sumOfMaxElements([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 18
    assert sumOfMaxElements([[10], [20], [30]]) == 60
    assert sumOfMaxElements([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == -18
    assert sumOfMaxElements([[5, 5, 5], [1, 1, 1], [10, 10, 10]]) == 25
    assert sumOfMaxElements([[100, 200], [-50, 50], [0, 0]]) == 250