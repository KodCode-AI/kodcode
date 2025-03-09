from solution import *

from solution import length_of_lis

def test_length_of_lis_with_empty_list():
    assert length_of_lis([]) == 0

def test_length_of_lis_with_single_element():
    assert length_of_lis([1]) == 1

def test_length_of_lis_with_constant_values():
    assert length_of_lis([1, 1, 1, 1]) == 1

def test_length_of_lis_with_multiple_elements():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_length_of_lis_with_reversed_increasing_sequence():
    assert length_of_lis([5, 4, 3, 2, 1]) == 1

def test_length_of_lis_with_random_sequence():
    assert length_of_lis([4, 2, 4, 3, 3, 1, 2, 1]) == 4