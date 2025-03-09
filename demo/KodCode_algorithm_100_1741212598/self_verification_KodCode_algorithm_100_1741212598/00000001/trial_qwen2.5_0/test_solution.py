from solution import *

import pytest
from heapq import nlargest, nsmallest

def test_insertion_sort():
    arr = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79]
    insertion_sort(arr, 2, 5)
    assert arr[2:6] == [6, 7, 8, 2, 8]  # Insertion sort from index 2 to 5

def test_intro_sort_small_size_threshold():
    array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79]
    intro_sort(array, 0, 5, 3, 2)
    assert array[0:6] == [1, 2, 4, 6, 7, 8]  # Insertion sort used for small array

def test_intro_sort_switch_to_heap():
    array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79]
    intro_sort(array, 6, 11, 3, 1)
    assert array[6:12] == [56, 79, 22, 14, 27, 8]  # Heapsort used due to max_depth

def test_intro_sort_comprehensive():
    array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79]
    intro_sort(array, 0, 11, 3, 3)
    assert array == [1, 2, 4, 6, 7, 8, 8, 14, 22, 27, 56, 79]  # Full Introsort process

def test_empty_array():
    array = []
    intro_sort(array, 0, 0, 3, 3)
    assert array == []  # Empty array check

def test_single_element_array():
    array = [1]
    intro_sort(array, 0, 0, 3, 3)
    assert array == [1]  # Single element array check

def test_repeated_elements():
    array = [2, 2, 2, 2, 2]
    intro_sort(array, 0, 4, 3, 3)
    assert array == [2, 2, 2, 2, 2]  # Repeated elements check