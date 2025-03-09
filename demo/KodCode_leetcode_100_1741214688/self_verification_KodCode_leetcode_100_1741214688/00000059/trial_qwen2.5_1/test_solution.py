from solution import *

def test_max_absolute_difference_sum():
    assert max_absolute_difference_sum([1, 2, 3, 4], [2, 1, 4, 3]) == 10
    assert max_absolute_difference_sum([1, 2, 3, 4, 5], [1, 4, 3, 2, 5]) == 10
    assert max_absolute_difference_sum([-1, -2, -3], [-2, -1, -4]) == 6
    assert max_absolute_difference_sum([1, 3, 5, 7], [8, 6, 4, 2]) == 18

def test_max_absolute_difference_sum_with_equal_elements():
    assert max_absolute_difference_sum([1, 1, 1], [1, 1, 1]) == 0
    assert max_absolute_difference_sum([-1, -1, -1], [-1, -1, -1]) == 0

def test_max_absolute_difference_sum_with_large_numbers():
    assert max_absolute_difference_sum([10, 100, 1000], [1, 0, 0]) == 1989
    assert max_absolute_difference_sum([500, 600, 700], [1000, 900, 800]) == 1300