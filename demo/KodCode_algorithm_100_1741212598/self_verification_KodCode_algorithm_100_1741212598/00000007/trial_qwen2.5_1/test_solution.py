from solution import *

import pytest

def test_search_value_in_matrix():
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert search_value_in_matrix(matrix, 1) == [0, 0]
    assert search_value_in_matrix(matrix, 20) == [-1, -1]
    assert search_value_in_matrix(matrix, 7) == [0, 2]
    assert search_value_in_matrix(matrix, 15) == [0, 4]

def test_search_matrix_empty():
    assert search_value_in_matrix([], 5) == [-1, -1]
    assert search_value_in_matrix([[]], 5) == [-1, -1]

def test_search_matrix_single_row():
    matrix = [[1, 3, 5]]
    assert search_value_in_matrix(matrix, 1) == [0, 0]
    assert search_value_in_matrix(matrix, 3) == [0, 1]
    assert search_value_in_matrix(matrix, 5) == [0, 2]
    assert search_value_in_matrix(matrix, 0) == [-1, -1]

def test_search_matrix_single_column():
    matrix = [[1], [2], [3], [4], [5]]
    assert search_value_in_matrix(matrix, 3) == [2, 0]
    assert search_value_in_matrix(matrix, 6) == [-1, -1]

def test_search_matrix_large():
    matrix = [[i + j * 100 for i in range(10)] for j in range(100)]
    for i in range(10):
        assert search_value_in_matrix(matrix, i * 100 + i) == [i, i]
    for value in range(1000, 100000):
        if value % 100 < 10:
            assert search_value_in_matrix(matrix, value) == [value // 100, value % 100]
        else:
            assert search_value_in_matrix(matrix, value) == [-1, -1]