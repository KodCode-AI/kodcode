from solution import *

from solution import sort_2d_list

def test_sort_2d_list_empty():
    assert sort_2d_list([]) == []

def test_sort_2d_list_single_element():
    assert sort_2d_list([[1, 2, 3]]) == [[1, 2, 3]]

def test_sort_2d_list_positive_elements():
    assert sort_2d_list([[1, 2, 3], [4, 5], [6]]) == [[6], [4, 5], [1, 2, 3]]

def test_sort_2d_list_negative_elements():
    assert sort_2d_list([[-1, -2, -3], [-4, -5], [-6]]) == [[-6], [-4, -5], [-1, -2, -3]]

def test_sort_2d_list_mixed_elements():
    assert sort_2d_list([[1, -1, 2], [-2, 2], [0]]) == [[0], [-2, 2], [1, -1, 2]]