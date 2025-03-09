from solution import *

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
    assert search_value_in_matrix(matrix, 11) == [0, 3]
    assert search_value_in_matrix(matrix, 23) == [4, 2]

test_search_value_in_matrix()