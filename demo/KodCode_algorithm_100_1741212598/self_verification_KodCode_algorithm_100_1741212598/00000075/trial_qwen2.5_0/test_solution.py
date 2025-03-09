from solution import *

import pytest

def test_max_subsequence_sum():
    assert max_subsequence_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subsequence_sum([-1, -2, -3, -4]) == -1
    assert max_subsequence_sum([1, 2, 3, 4]) == 10
    assert max_subsequence_sum([0]) == 0
    assert max_subsequence_sum([-100, -200, 1, 2, 3, -50]) == 6
    assert max_subsequence_sum([-2, -3, -1]) == -1
    assert max_subsequence_sum([5, -1, 5, 4, -7]) == 11
    assert max_subsequence_sum([-1, 2, 3, -4, 5]) == 8
    assert max_subsequence_sum([1, -1, 1, -1, 1]) == 1
    assert max_subsequence_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7

pytest.main(['-v', 'solution.py'])