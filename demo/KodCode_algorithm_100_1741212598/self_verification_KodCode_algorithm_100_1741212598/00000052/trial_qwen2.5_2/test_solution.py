from solution import *

import pytest

def test_find_next_power_of_two():
    # Test with edge case
    assert find_next_power_of_two(0) == 1
    # Test with smallest power of two
    assert find_next_power_of_two(1) == 2
    # Test with a number that is already a power of two
    assert find_next_power_of_two(16) == 32
    # Test with a number that's in between two powers of two
    assert find_next_power_of_two(15) == 16
    # Test with a larger number
    assert find_next_power_of_two(100) == 128
    # Test with the maximum possible input
    assert find_next_power_of_two(10**9) == 1073741824

if __name__ == "__main__":
    pytest.main()