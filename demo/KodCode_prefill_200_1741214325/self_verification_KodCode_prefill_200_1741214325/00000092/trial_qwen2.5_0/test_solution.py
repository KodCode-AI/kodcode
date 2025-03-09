from solution import *

from solution import sort_tuples_list

def test_sort_tuples_list():
    assert sort_tuples_list([(1, 3), (4, 1), (5, 2), (3, 2)]) == [(4, 1), (3, 2), (5, 2), (1, 3)]
    assert sort_tuples_list([(2, 5), (3, 4), (1, 4), (4, 5)]) == [(1, 4), (3, 4), (2, 5), (4, 5)]
    assert sort_tuples_list([(2, 2), (3, 2), (1, 2)]) == [(1, 2), (2, 2), (3, 2)]
    assert sort_tuples_list([(4, 10), (5, 2), (1, 3)]) == [(1, 3), (5, 2), (4, 10)]
    assert sort_tuples_list([]) == []
    assert sort_tuples_list([(1, 1)]) == [(1, 1)]