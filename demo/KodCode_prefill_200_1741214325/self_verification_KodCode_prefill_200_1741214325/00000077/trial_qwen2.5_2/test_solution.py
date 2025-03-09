from solution import *

from solution import sort_2d_list

def test_sort_2d_list_with_negative_and_positive_integers():
    input_list = [[3, 5, -2], [2, 5], [3, 1, -4]]
    expected_output = [[2, 5], [3, 1, -4], [3, 5, -2]]
    assert sort_2d_list(input_list) == expected_output

def test_sort_2d_list_with_all_positive_integers():
    input_list = [[2, 3, 5], [5, 7], [1, 2]]
    expected_output = [[1, 2], [2, 3, 5], [5, 7]]
    assert sort_2d_list(input_list) == expected_output

def test_sort_2d_list_with_all_zeros():
    input_list = [[], [0, 0, 0], [0]]
    expected_output = [[], [0], [0, 0, 0]]
    assert sort_2d_list(input_list) == expected_output

def test_sort_2d_list_with_single_element_lists():
    input_list = [[3], [7], [1, 2]]
    expected_output = [[3], [1, 2], [7]]
    assert sort_2d_list(input_list) == expected_output

def test_sort_2d_list_with_empty_lists():
    input_list = [[], [], []]
    expected_output = [[], [], []]
    assert sort_2d_list(input_list) == expected_output

def test_sort_2d_list_with_mixed_sublists():
    input_list = [[2, -1], [3, -3, 2], [], [-3, -2]]
    expected_output = [[], [-3, -2], [2, -1], [3, -3, 2]]
    assert sort_2d_list(input_list) == expected_output