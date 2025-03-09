from solution import *

import pytest

def test_max_monotonic_group_size():
    assert max_monotonic_group_size([5, 4, 3, 2, 1, 2, 3, 4, 5]) == 5
    assert max_monotonic_group_size([1, 3, 5, 4, 2, 4, 6]) == 4
    assert max_monotonic_group_size([1, 2, 3, 4, 5, 6]) == 6
    assert max_monotonic_group_size([6, 5, 4, 3, 2, 1]) == 6
    assert max_monotonic_group_size([1, 3, 2, 2, 3, 4, 5]) == 3
    assert max_monotonic_group_size([1]) == 1
    assert max_monotonic_group_size([1, 2, 3, 2, 1]) == 3

pytest.main(['-v', __file__])