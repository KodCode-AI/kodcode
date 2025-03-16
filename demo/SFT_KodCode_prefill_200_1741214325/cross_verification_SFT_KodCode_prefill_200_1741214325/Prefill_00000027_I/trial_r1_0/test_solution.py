from solution import *

def test_union_of_lists():
    assert union_of_lists([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 4, 5]
    assert union_of_lists([1, 2, 2, 3], [3, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert union_of_lists([], [1, 2, 3]) == [1, 2, 3]
    assert union_of_lists([1, 2, 3], []) == [1, 2, 3]
    assert union_of_lists([], []) == []