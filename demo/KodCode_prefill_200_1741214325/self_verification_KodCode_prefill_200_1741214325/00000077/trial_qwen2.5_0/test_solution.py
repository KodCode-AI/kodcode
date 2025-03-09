from solution import *

def test_sort_2d_list():
    test_list = [[3, 5, 2], [1, 2], [4, 1, 3]]
    expected_result = [[1, 2], [3, 5, 2], [4, 1, 3]]
    assert sort_2d_list(test_list) == expected_result

def test_sort_2d_list_with_zeros():
    test_list = [[0, 0, 0], [1, 0], [0, 1]]
    expected_result = [[0, 0, 0], [1, 0], [0, 1]]
    assert sort_2d_list(test_list) == expected_result

def test_sort_2d_list_with_negative_numbers():
    test_list = [[-1, -2, -3], [-2, -1], [-3, -1, -2]]
    expected_result = [[-3, -2, -1], [-2, -1], [-3, -1, -2]]
    assert sort_2d_list(test_list) == expected_result

def test_sort_2d_list_with_mixed_sign_numbers():
    test_list = [[2, -1, -3], [0, 1], [-2, 3, 1]]
    expected_result = [[0, 1], [2, -1, -3], [-2, 3, 1]]
    assert sort_2d_list(test_list) == expected_result