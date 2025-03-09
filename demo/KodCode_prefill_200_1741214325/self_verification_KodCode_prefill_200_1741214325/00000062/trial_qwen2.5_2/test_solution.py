from solution import *

from solution import second_maximum

def test_second_maximum_with_two_unique_numbers():
    assert second_maximum([1, 2]) == 1

def test_second_maximum_with_sorted_repeating_numbers():
    assert second_maximum([5, 5, 4, 4, 3, 3]) == 4

def test_second_maximum_with_descending_repeating_numbers():
    assert second_maximum([10, 9, 10, 9]) == 9

def test_second_maximum_with_no_enough_unique_numbers():
    assert second_maximum([2, 2]) == None

def test_second_maximum_with_random_numbers():
    assert second_maximum([7, 8, 9, 10, 11, 9]) == 10

def test_second_maximum_with_only_one_number():
    assert second_maximum([100]) == None

def test_second_maximum_with_empty_list():
    assert second_maximum([]) == None