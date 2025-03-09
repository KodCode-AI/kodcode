from solution import *

def test_max_value_after_shift():
    assert max_value_after_shift([2, 3, 1, 4, 0], 3) == 10
    assert max_value_after_shift([10, 1], 0) == 18
    assert max_value_after_shift([2, 2, 2], 1) == 2
    assert max_value_after_shift([1, 10, 100], 2) == 207
    assert max_value_after_shift([1], 10) == 0
    assert max_value_after_shift([1, 1, 1], 1) == 2
    assert max_value_after_shift([1, 1, 1], 2) == 2
    assert max_value_after_shift([1, 1, 1, 1, 1, 1], 3) == 0