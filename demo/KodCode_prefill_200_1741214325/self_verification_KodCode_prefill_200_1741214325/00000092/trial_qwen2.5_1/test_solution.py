from solution import *

from solution import sort_tuples_by_second_item

def test_sort_tuples_by_second_item():
    assert sort_tuples_by_second_item([(1, 3), (4, 1), (5, 2), (3, 2)]) == [(4, 1), (5, 2), (3, 2), (1, 3)]
    assert sort_tuples_by_second_item([(2, 2), (3, 1), (1, 1)]) == [(3, 1), (1, 1), (2, 2)]
    assert sort_tuples_by_second_item([(1, 1), (2, 1), (3, 1)]) == [(1, 1), (2, 1), (3, 1)]
    assert sort_tuples_by_second_item([(4, 2), (5, 2), (2, 1)]) == [(2, 1), (4, 2), (5, 2)]