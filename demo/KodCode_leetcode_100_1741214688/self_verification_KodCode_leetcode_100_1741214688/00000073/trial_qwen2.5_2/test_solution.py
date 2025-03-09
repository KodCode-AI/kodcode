from solution import *

from solution import longest_snake

def test_longest_snake_example1():
    grid = [
        [0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1]
    ]
    assert longest_snake(grid) == 6

def test_longest_snake_example2():
    grid = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    assert longest_snake(grid) == 5

def test_longest_snake_example3():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 1, 0, 0, 0]
    ]
    assert longest_snake(grid) == 0
    # Starting point is water, so no snake is formed

def test_longest_snake_example4():
    grid = [
        [1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0]
    ]
    assert longest_snake(grid) == 4