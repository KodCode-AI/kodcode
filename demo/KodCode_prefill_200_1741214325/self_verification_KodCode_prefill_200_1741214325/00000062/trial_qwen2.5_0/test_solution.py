from solution import *

from solution import second_maximum

def test_second_maximum_with_multiple_different_numbers():
    assert second_maximum([1, 3, 5, 7, 9]) == 7
    assert second_maximum([10, 5, 10, 7, 10]) == 7

def test_second_maximum_with_one_unique_number():
    assert second_maximum([5, 5, 5, 5]) == None

def test_second_maximum_with_no_numbers():
    assert second_maximum([]) == None

def test_second_maximum_with_one_number():
    assert second_maximum([5]) == None

def test_second_maximum_with_duplicates():
    assert second_maximum([2, 2, 3, 5, 5]) == 3
    assert second_maximum([1, 1, 4, 4, 10, 10]) == 4

def test_second_maximum_SINGLE_NUMBER():
    assert second_maximum([9]) == None