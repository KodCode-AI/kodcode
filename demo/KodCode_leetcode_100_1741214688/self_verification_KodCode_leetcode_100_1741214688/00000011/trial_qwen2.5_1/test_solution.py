from solution import *

from solution import has_path_with_target

def test_has_path_with_target():
    grid1 = [[1, 3, 2], [1, 5, 1], [4, 2, 1]]
    target1 = 8
    assert has_path_with_target(grid1, target1) == True

    grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target2 = 20
    assert has_path_with_target(grid2, target2) == True

    grid3 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    target3 = 13
    assert has_path_with_target(grid3, target3) == False

    grid4 = [[1, 5, 1], [1, -2, 1], [4, 2, -1]]
    target4 = 7
    assert has_path_with_target(grid4, target4) == False

    grid5 = [[1, 3], [2, 2], [3, 1], [4, 0]]
    target5 = 10
    assert has_path_with_target(grid5, target5) == True

    grid6 = [[1, 3, 2], [1, -1, 1], [4, -1, 1]]
    target6 = 7
    assert has_path_with_target(grid6, target6) == True

    grid7 = [[2, 3, 1], [1, 4, 1], [1, 1, 1]]
    target7 = 15
    assert has_path_with_target(grid7, target7) == False

    grid8 = [[3, 9, 4]]
    target8 = 11
    assert has_path_with_target(grid8, target8) == True

    grid9 = [[1, 2]]
    target9 = 3
    assert has_path_with_target(grid9, target9) == True

    grid10 = [[1]]
    target10 = 1
    assert has_path_with_target(grid10, target10) == True