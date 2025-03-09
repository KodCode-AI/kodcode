from solution import *

import pytest

def test_maxNumberOfIslands():
    grid = [[0,0],[1,1]]
    assert maxNumberOfIslands(grid) == 1

def test_maxNumberOfIslands_with_islands():
    grid = [[0,1],[1,0]]
    assert maxNumberOfIslands(grid) == 2

def test_maxNumberOfIslands_single_island():
    grid = [[1,1],[1,1]]
    assert maxNumberOfIslands(grid) == 1

def test_maxNumberOfIslands_all_ones():
    grid = [[1,1,1],[1,1,1],[1,1,1]]
    assert maxNumberOfIslands(grid) == 1

def test_maxNumberOfIslands_no_islands():
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    assert maxNumberOfIslands(grid) == 0

def test_maxNumberOfIslands_with_void():
    grid = [[1,1,0],[0,0,0],[1,0,1]]
    assert maxNumberOfIslands(grid) == 1