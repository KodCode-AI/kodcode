from solution import *

from solution import maxNumberOfIslands

def test_maxNumberOfIslands_empty_grid():
    assert maxNumberOfIslands([]) == 0

def test_maxNumberOfIslands_one_island():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert maxNumberOfIslands(grid) == 3

def test_maxNumberOfIslands_no_islands():
    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert maxNumberOfIslands(grid) == 0

def test_maxNumberOfIslands_all_islands():
    grid = [
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"],
        ["1", "0", "1", "0", "1"],
        ["0", "1", "0", "1", "0"]
    ]
    assert maxNumberOfIslands(grid) == 4

def test_maxNumberOfIslands_complex_grid():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "1", "0"],
        ["0", "0", "1", "1", "0"],
        ["0", "0", "0", "0", "1"]
    ]
    assert maxNumberOfIslands(grid) == 1