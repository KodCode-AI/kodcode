from solution import *

def test_sum_even_sublists():
    assert sum_even_sublists([[1, 2, 3], [4, 5, 6, 7], [8]]) == 18
    assert sum_even_sublists([[1, 2], []]) == 3
    assert sum_even_sublists([[1], [2, 3, 4], [5, 6, 7, 8], [9]]) == 30
    assert sum_even_sublists([[10, 20, 30], [40], [50, 60]]) == 100
    assert sum_even_sublists([]) == 0
    assert sum_even_sublists([[1, 2], [3, 4], [5, 6], [7]]) == 18