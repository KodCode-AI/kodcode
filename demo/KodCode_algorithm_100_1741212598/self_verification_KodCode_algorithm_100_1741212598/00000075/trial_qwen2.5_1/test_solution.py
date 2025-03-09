from solution import *

python
import pytest

def test_max_subsequence_sum():
    assert max_subsequence_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subsequence_sum([-1, -2, -3, -4]) == -1
    assert max_subsequence_sum([1, 2, 3, 4]) == 10
    assert max_subsequence_sum([0]) == 0
    assert max_subsequence_sum([-10, 2, 3, -2, 0, 5, -1]) == 12
    assert max_subsequence_sum([-100, 201, -200, 202]) == 203
    assert max_subsequence_sum([-10, -20, -30, -40]) == -10
    assert max_subsequence_sum([10, -30, 40, -50, 60]) == 80