from solution import *

python
def test_quick_sort():
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort(arr)
    expected = [1, 1, 2, 3, 6, 8, 10]
    assert sorted_arr == expected

def test_quick_sort_empty():
    arr = []
    sorted_arr = quick_sort(arr)
    expected = []
    assert sorted_arr == expected

def test_quick_sort_single_element():
    arr = [5]
    sorted_arr = quick_sort(arr)
    expected = [5]
    assert sorted_arr == expected

def test_quick_sort_negative_numbers():
    arr = [3, -1, -12, 0, 15, 4]
    sorted_arr = quick_sort(arr)
    expected = [-12, -1, 0, 3, 4, 15]
    assert sorted_arr == expected

def test_quick_sort_duplicate_elements():
    arr = [4, 4, 4, 4, 4]
    sorted_arr = quick_sort(arr)
    expected = [4, 4, 4, 4, 4]
    assert sorted_arr == expected

def test_quick_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    sorted_arr = quick_sort(arr)
    expected = [1, 2, 3, 4, 5]
    assert sorted_arr == expected