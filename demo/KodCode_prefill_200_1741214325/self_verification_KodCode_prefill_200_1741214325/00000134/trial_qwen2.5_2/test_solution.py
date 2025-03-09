from solution import *

def test_second_smallest():
    assert second_smallest([3, 5, 2, 2, 8, 1, 1, 4]) == 3
    assert second_smallest([1, 1]) == None
    assert second_smallest([5]) == None
    assert second_smallest([2, 2, 2, 2, 2]) == None
    assert second_smallest([10, 9, 8, 10, 8, 10, 8]) == 9
    assert second_smallest([7, 7, 6, 6, 5, 4, 4, 3, 2, 1]) == 6