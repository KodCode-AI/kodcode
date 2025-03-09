from solution import *

``
def test_max_subsequence_sum():
    assert max_subsequence_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subsequence_sum([-1, -2, -3, -4]) == -1
    assert max_subsequence_sum([1, 2, 3, 4]) == 10
    assert max_subsequence_sum([0]) == 0
    assert max_subsequence_sum([-2, -1, -3, -4, -1, -2, -3, -4]) == -1
    assert max_subsequence_sum([2, -1, 2, 3, 4, -5]) == 10

# Run tests
test_max_subsequence_sum()