from solution import *

def test_find_smallest_path():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 3
    assert find_smallest_path(grid, k) == [1, 2, 4]
    
    grid = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
    k = 2
    assert find_smallest_path(grid, k) == [1, 2]

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 4
    assert find_smallest_path(grid, k) == [1, 2, 4, 7]

    grid = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
    k = 3
    assert find_smallest_path(grid, k) == [10, 11, 12]

    grid = [[1, 1, 3], [4, 5, 6], [7, 8, 2]]
    k = 2
    assert find_smallest_path(grid, k) == [1, 1]

    grid = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    k = 2
    assert find_smallest_path(grid, k) == [1, 1]

    grid = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    k = 3
    assert find_smallest_path(grid, k) == [1, 2, 3]

    grid = [[9, 8, 7], [4, 5, 6], [3, 2, 1]]
    k = 3
    assert find_smallest_path(grid, k) == [1, 2, 1]