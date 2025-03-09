from solution import *

def test_min_steps_to_position():
    assert min_steps_to_position([1, 2, 3], [[2], [3], [1]], 1) == 4
    assert min_steps_to_position([1, 2, 3], [[2], [3], [1]], 2) == 2
    assert min_steps_to_position([1, 2, 3], [[2], [3], [1]], 0) == -1
    assert min_steps_to_position([1, 2, 3], [[2], [3]], 1) == -1
    assert min_steps_to_position([1, 2, 3], [[2], [4], [5]], 2) == -1
    assert min_steps_to_position([1, 2], [[1], [2]], 1) == 1