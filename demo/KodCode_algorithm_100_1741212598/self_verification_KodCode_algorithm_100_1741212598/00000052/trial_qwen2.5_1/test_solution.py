from solution import *

import pytest

def test_find_next_power_of_two():
    assert find_next_power_of_two(0) == 1
    assert find_next_power_of_two(1) == 2
    assert find_next_power_of_two(15) == 16
    assert find_next_power_of_two(16) == 32
    assert find_next_power_of_two(1023) == 1024
    assert find_next_power_of_two(1024) == 2048
    assert find_next_power_of_two(1048575) == 1048576
    assert find_next_power_of_two(1048576) == 2097152
    pytest.approx(find_next_power_of_two(999999999), 2_000_000_000)