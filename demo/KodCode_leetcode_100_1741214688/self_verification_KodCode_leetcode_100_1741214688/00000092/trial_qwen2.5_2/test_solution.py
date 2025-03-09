from solution import *

import pytest

def test_shortest_border_path():
    grid1 = ['S#L', 'LLL', 'LWL']
    assert shortest_border_path(grid1) == 1

    grid2 = ['W', 'L', 'L', 'L']
    assert shortest_border_path(grid2) == -1

    grid3 = ['L', 'L', 'L', 'S']
    assert shortest_border_path(grid3) == 0

    grid4 = ['SWL', 'LWL', 'LWL']
    assert shortest_border_path(grid4) == 1

    grid5 = ['LWL', 'SLL', 'WLW', 'WWW']
    assert shortest_border_path(grid5) == 2

    grid6 = ['W']
    assert shortest_border_path(grid6) == -1

    grid7 = ['S']
    assert shortest_border_path(grid7) == 0

    grid8 = ['L', 'S', 'L', 'L', 'L', 'L']
    assert shortest_border_path(grid8) == 1

    grid9 = ['L', 'L', 'L', 'L', 'L', 'S']
    assert shortest_border_path(grid9) == 0

    grid10 = ['L', 'S', 'L', 'L', 'L', 'L']
    assert shortest_border_path(grid10) == 1

    grid11 = ['L', 'L', 'L', 'L', 'L', 'L', 'S']
    assert shortest_border_path(grid11) == 0

    grid12 = ['L', 'S', 'L', 'L']
    assert shortest_border_path(grid12) == 1

    grid13 = ['S', 'L', 'L', 'L']
    assert shortest_border_path(grid13) == 0

    grid14 = ['L', 'L', 'L', 'S']
    assert shortest_border_path(grid14) == 1

    grid15 = ['S', 'S', 'S', 'S']
    assert shortest_border_path(grid15) == -1

    grid16 = ['L', 'L', 'L', 'L', 'L', 'L', 'S', 'L', 'L', 'L']
    assert shortest_border_path(grid16) == 3

    grid17 = ['L', 'L', 'L', 'L', 'L', 'L', 'S', 'L', 'L', 'L', 'L']
    assert shortest_border_path(grid17) == 2

    grid18 = ['S', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
    assert shortest_border_path(grid18) == 0

    grid19 = ['L', 'L', 'L', 'S', 'L', 'L', 'L', 'L', 'L', 'L']
    assert shortest_border_path(grid19) == 1

    grid20 = ['L', 'L', 'L', 'L', 'L', 'L', 'S', 'L', 'L', 'L', 'L', 'L']
    assert shortest_border_path(grid20) == 3