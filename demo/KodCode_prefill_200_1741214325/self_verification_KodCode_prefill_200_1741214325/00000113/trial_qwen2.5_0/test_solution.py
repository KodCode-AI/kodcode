from solution import *

from solution import largest_rectangle_in_histogram

# Test cases to verify the solution
def test_case1():
    assert largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3]) == 10

def test_case2():
    assert largest_rectangle_in_histogram([2, 4]) == 4

def test_case3():
    assert largest_rectangle_in_histogram([3, 1, 3]) == 6

def test_case4():
    assert largest_rectangle_in_histogram([1, 2, 3, 4, 5]) == 9

def test_case5():
    assert largest_rectangle_in_histogram([0, 0, 0, 0]) == 0

def test_case6():
    assert largest_rectangle_in_histogram([1]) == 1

def test_case7():
    assert largest_rectangle_in_histogram([6, 2, 5, 4, 5, 1, 6]) == 12