from solution import *

from solution import largest_rectangle_in_histogram

def test_rectangle_single_bar():
    heights = [5]
    expected_area = 5
    assert largest_rectangle_in_histogram(heights) == expected_area

def test_rectangle_two_tall_bars():
    heights = [2, 2]
    expected_area = 4
    assert largest_rectangle_in_histogram(heights) == expected_area

def test_rectangle_decreasing_heights():
    heights = [2, 1, 5, 6, 2, 3]
    expected_area = 10
    # The largest rectangle is formed by the last two bars with height 5 and 6
    assert largest_rectangle_in_histogram(heights) == expected_area

def test_rectangle_mixed_heights():
    heights = [1, 3, 1, 4, 2, 1]
    expected_area = 6
    assert largest_rectangle_in_histogram(heights) == expected_area

def test_rectangle_downwards_slope():
    heights = [6, 2, 5, 4, 5, 1, 6]
    expected_area = 12
    assert largest_rectangle_in_histogram(heights) == expected_area

def test_rectangle_all_zero():
    heights = [0, 0, 0, 0]
    expected_area = 0
    assert largest_rectangle_in_histogram(heights) == expected_area

def test_rectangle_all_same_height():
    heights = [5, 5, 5, 5]
    expected_area = 16
    assert largest_rectangle_in_histogram(heights) == expected_area