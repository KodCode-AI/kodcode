from solution import *

from pytest import fixture, mark
from random import shuffle

@fixture
def shuffled_list():
    return list(range(10000))
    shuffle(shuffled_list)

def test_introsort(shuffled_list):
    for size_threshold in [1, 10, 100]:
        for max_depth in [1, 10, 100]:
            sorted_list = shuffled_list.copy()
            sorted_list.sort()
            assert intro_sort(sorted_list, 0, len(sorted_list) - 1, size_threshold, max_depth) == sorted_list

def test_insertion_sort():
    array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79]
    start = 0
    end = len(array) - 1
    size_threshold = 16
    assert intro_sort(array, start, end, size_threshold, 10) == sorted(array)

def test_partition():
    array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79]
    end = len(array) - 1
    pivot_index = partition(array, 0, end)
    assert pivot_index == 6 and array == [1, 2, 4, 6, 7, 8, 8, 14, 22, 56, 27, 79]

def test_introsort_worst_case():
    array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    size_threshold = 1
    max_depth = 10
    assert intro_sort(array, 0, len(array) - 1, size_threshold, max_depth) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_introsort_best_case():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    size_threshold = 1
    max_depth = 10
    assert intro_sort(array, 0, len(array) - 1, size_threshold, max_depth) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]