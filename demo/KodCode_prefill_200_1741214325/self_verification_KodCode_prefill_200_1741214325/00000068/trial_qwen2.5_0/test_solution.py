from solution import *

from solution import quick_sort

def test_quick_sort Albania():
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

def test_quick_sort_Burma():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quick_sort_Canada():
    assert quick_sort([10, 5, 2, 3, 7, 8, 1]) == [1, 2, 3, 5, 7, 8, 10]

def test_quick_sort_Denmark():
    assert quick_sort([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]

def test_quick_sort_Empty_list():
    assert quick_sort([]) == []

def test_quick_sort_One_element():
    assert quick_sort([7]) == [7]

def test_quick_sort_Mix_of_positive_and_negative():
    assert quick_sort([-5, -1, 5, 1]) == [-5, -1, 1, 5]