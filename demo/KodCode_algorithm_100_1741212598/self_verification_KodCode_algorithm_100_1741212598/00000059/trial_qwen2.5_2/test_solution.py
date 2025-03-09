from solution import *

def test_custom_selection_sort():
    assert custom_selection_sort([]) == []
    assert custom_selection_sort([9, 4, 2, 1, 5, 3]) == [3, 4, 2, 1, 5, 9]
    assert custom_selection_sort([1, 3, 5, 7]) == [1, 3, 5, 7]
    assert custom_selection_sort([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert custom_selection_sort([4, 1, 3, 2]) == [2, 1, 3, 4]
    assert custom_selection_sort([11, 22, 33, 44, 55, 66]) == [55, 22, 33, 44, 11, 66]