from solution import *

import pytest

def test_minimum_time_to_complete():
    assert minimum_time_to_complete([1, 2, 3, 4], 2) == 6
    assert minimum_time_to_complete([9, 2, 2, 2, 2, 2, 7], 5) == 15
    assert minimum_time_to_complete([1, 1, 1], 1) == 2
    assert minimum_time_to_complete([10], 0) == 10
    assert minimum_time_to_complete([2, 6, 3, 1, 2, 5], 3) == 10

if __name__ == "__main__":
    pytest.main()