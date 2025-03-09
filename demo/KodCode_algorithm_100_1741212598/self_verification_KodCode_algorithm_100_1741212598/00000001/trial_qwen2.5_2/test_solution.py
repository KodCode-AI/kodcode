from solution import *

import random

def test_intro_sort():
    array = [random.randint(1, 100) for _ in range(100)]
    start = random.randint(0, len(array) // 2)
    end = random.randint(start + 1, len(array) - 1)
    size_threshold = 16
    max_depth = 50
    sorted_array = sorted(array[start:end + 1])
    assert intro_sort(array, start, end, size_threshold, max_depth) == sorted_array

def test_single_element():
    array = [42]
    start = 0
    end = 0
    size_threshold = 16
    max_depth = 50
    assert intro_sort(array, start, end, size_threshold, max_depth) == [42]

def test_empty_subarray():
    array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79]
    start = 3
    end = 2
    size_threshold = 16
    max_depth = 50
    assert intro_sort(array, start, end, size_threshold, max_depth) == []

def test_larger_arrays():
    array = [random.randint(1, 100) for _ in range(1000)]
    start = len(array) // 2
    end = len(array) - 1
    size_threshold = 16
    max_depth = 50
    sorted_array = sorted(array[start:end + 1])
    assert intro_sort(array, start, end, size_threshold, max_depth) == sorted_array

def test_repeated_elements():
    array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 79]
    start = 0
    end = len(array) - 1
    size_threshold = 16
    max_depth = 50
    sorted_array = sorted(array[start:end + 1])
    assert intro_sort(array, start, end, size_threshold, max_depth) == sorted_array