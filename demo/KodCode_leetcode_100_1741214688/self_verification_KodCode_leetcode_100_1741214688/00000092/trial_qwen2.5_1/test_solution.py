from solution import *

def test_shortest_path_to_border():
    grid = [
        ['L', 'L', 'L'],
        ['L', 'S', 'L'],
        ['L', 'L', 'L']
    ]
    assert shortest_path_to_border(grid) == 0

    grid = [
        ['L', 'L', 'L'],
        ['W', 'S', 'L'],
        ['L', 'L', 'L']
    ]
    assert shortest_path_to_border(grid) == 1

    grid = [
        ['L', 'L', 'L'],
        ['L', 'S', 'W'],
        ['L', 'L', 'L']
    ]
    assert shortest_path_to_border(grid) == -1

    grid = [
        ['W', 'L', 'L'],
        ['L', 'S', 'L'],
        ['L', 'L', 'W']
    ]
    assert shortest_path_to_border(grid) == 2

    grid = [
        ['L', 'W', 'L'],
        ['L', 'S', 'L'],
        ['W', 'L', 'L']
    ]
    assert shortest_path_to_border(grid) == -1

    grid = [
        ['L', 'L', 'L', 'W'],
        ['L', 'S', 'L', 'L'],
        ['L', 'L', 'L', 'L']
    ]
    assert shortest_path_to_border(grid) == 1

    grid = [
        ['W', 'W', 'W'],
        ['W', 'S', 'W'],
        ['W', 'W', 'W']
    ]
    assert shortest_path_to_border(grid) == -1