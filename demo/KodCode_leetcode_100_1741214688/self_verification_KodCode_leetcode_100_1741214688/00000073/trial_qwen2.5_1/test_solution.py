from solution import *

import pytest

def test_max_snake_length():
    grid1 = [[0,1,1,1,0,0,0],[0,1,0,1,1,1,0]]
    assert max_snake_length(grid1) == 4

    grid2 = [[0,1,1,1,1]]
    assert max_snake_length(grid2) == 3

    grid3 = [[0,0,0,0]]
    assert max_snake_length(grid3) == 0

    grid4 = [[1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]]
    assert max_snake_length(grid4) == 8

    grid5 = [[1,1,1],[0,0,1],[1,1,1]]
    assert max_snake_length(grid5) == 5