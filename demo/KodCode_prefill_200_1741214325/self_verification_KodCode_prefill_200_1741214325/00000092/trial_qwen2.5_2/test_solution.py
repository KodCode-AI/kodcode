from solution import *

def test_sort_tuples():
    assert sort_tuples([(1, 3), (4, 1), (5, 2), (3, 2)]) == [(4, 1), (3, 2), (5, 2), (1, 3)]
    assert sort_tuples([(2, 2), (3, 1), (1, 2), (4, 1)]) == [(3, 1), (4, 1), (1, 2), (2, 2)]
    assert sort_tuples([(1, 5), (2, 4), (3, 4)]) == [(2, 4), (3, 4), (1, 5)]
    assert sort_tuples([(1, 1), (2, 2), (3, 1)]) == [(1, 1), (3, 1), (2, 2)]
    assert sort_tuples([(10, 10), (5, 5), (7, 8)]) == [(5, 5), (7, 8), (10, 10)]