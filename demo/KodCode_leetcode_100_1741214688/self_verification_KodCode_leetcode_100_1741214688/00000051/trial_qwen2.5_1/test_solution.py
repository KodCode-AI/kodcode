from solution import *

from solution import CustomComparator

def test_custom_comparator():
    comparator = CustomComparator([10, 11, 12, 13, 14, 15, 16, 17])
    comparator.sort()
    assert comparator.get_result() == [10, 17, 12, 15, 14, 13, 16, 11]

def test_empty_array():
    comparator = CustomComparator([])
    comparator.sort()
    assert comparator.get_result() == []

def test_single_element_array():
    comparator = CustomComparator([1])
    comparator.sort()
    assert comparator.get_result() == [1]

def test_odd_element_array():
    comparator = CustomComparator([10, 11, 12])
    comparator.sort()
    assert comparator.get_result() == [10, 12, 11]

def test_all_even_indices_same():
    comparator = CustomComparator([10, 10, 10, 10])
    comparator.sort()
    assert comparator.get_result() == [10, 10, 10, 10]

def test_all_odd_indices_same():
    comparator = CustomComparator([10, 20, 10, 20])
    comparator.sort()
    assert comparator.get_result() == [10, 20, 10, 20]