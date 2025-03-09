from solution import *

def test_max_islands():
    grid = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    assert max_islands(grid) == 7

def test_max_islands_with_single_island():
    grid = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    assert max_islands(grid) == 1

def test_max_islands_with_no_islands():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert max_islands(grid) == 0

def test_max_islands_with_separate_islands():
    grid = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    assert max_islands(grid) == 9