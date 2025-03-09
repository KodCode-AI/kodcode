from solution import *

def test_shortest_land_distance():
    # Test 1
    grid = [
        ['W', 'W', 'L'],
        ['L', 'S', 'L'],
        ['W', 'W', 'L']
    ]
    assert shortest_land_distance(grid) == 2

    # Test 2
    grid = [
        ['W', 'L', 'L'],
        ['L', 'S', 'L'],
        ['W', 'W', 'W']
    ]
    assert shortest_land_distance(grid) == 1

    # Test 3
    grid = [
        ['W', 'W', 'W'],
        ['W', 'S', 'W'],
        ['W', 'W', 'W']
    ]
    assert shortest_land_distance(grid) == -1

    # Test 4
    grid = [
        ['W', 'W', 'W'],
        ['L', 'S', 'L'],
        ['W', 'W', 'W']
    ]
    assert shortest_land_distance(grid) == -1

    # Test 5
    grid = [
        ['L', 'W', 'W'],
        ['L', 'L', 'S'],
        ['W', 'L', 'W']
    ]
    assert shortest_land_distance(grid) == 2

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])