from solution import *

from solution import insertion_sort

def test_insertion_sort_positive_numbers():
    arr = [9, 5, 1, 4, 3]
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == [1, 3, 4, 5, 9]

def test_insertion_sort_negative_numbers():
    arr = [-5, -9, -3, -4]
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == [-9, -5, -4, -3]

def test_insertion_sort_mixed_numbers():
    arr = [0, -1, 5, -2, 3]
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == [-2, -1, 0, 3, 5]

def test_insertion_sort_empty_list():
    arr = []
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == []

def test_insertion_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    sorted_arr = insertion_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5]