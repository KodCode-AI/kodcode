from solution import *

import pytest

def test_min_landlock_flips():
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    assert min_landlock_flips(grid) == 2

    grid = [[0, 0, 0], [0, 1, 1], [0, 1, 0]]
    assert min_landlock_flips(grid) == -1

    grid = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
    assert min_landlock_flips(grid) == -1

    grid = [[0, 0, 1], [0, 1, 0]]
    assert min_landlock_flips(grid) == 1

    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    assert min_landlock_flips(grid) == 1

    grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    assert min_landlock_flips(grid) == 2

# To run these tests, you need to have the above solution function defined in your solution.py file.
# Run the tests using pytest:
# pytest -q <path_to_your_test_file>.py