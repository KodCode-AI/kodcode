from solution import *

def test_min_steps_to_positions():
    assert min_steps_to_positions([2, 2, 3, 3], [2, 3], 2) == 4
    assert min_steps_to_positions([2, 2, 2], [2, 2, 2], 2) == -1
    assert min_steps_to_positions([1, 1, 2, 3], [1, 2, 3], 3) == 2
    assert min_steps_to_positions([4], [1], 1) == -1
    assert min_steps_to_positions([1, 2, 3], [1, 2, 3], 3) == 0

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])