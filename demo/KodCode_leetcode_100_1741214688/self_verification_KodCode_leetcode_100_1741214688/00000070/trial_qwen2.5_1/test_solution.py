from solution import *

def test_min_steps_to_positions():
    assert min_steps_to_positions(3, 2, [[2, 1, 3], [], []]) == 2
    assert min_steps_to_positions(3, 2, [[2, 1, 3], [2, 3, 1], [1, 3, 2]]) == -1
    assert min_steps_to_positions(5, 3, [[4, 1, 5], [4, 5, 1], [], [3, 5, 1], []]) == 4
    assert min_steps_to_positions(4, 2, [[2, 1], [], [3, 4], []]) == 2
    assert min_steps_to_positions(3, 1, [[2, 1, 3], [2, 3, 1], [1, 3, 2]]) == 2

test_min_steps_to_positions()