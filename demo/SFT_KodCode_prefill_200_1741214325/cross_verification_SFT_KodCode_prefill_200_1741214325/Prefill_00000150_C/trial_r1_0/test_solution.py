from solution import *

def test_is_power_of_two():
    assert not is_power_of_two(-4)
    assert not is_power_of_two(0)
    assert is_power_of_two(1)
    assert is_power_of_two(2)
    assert is_power_of_two(4)
    assert not is_power_of_two(3)
    assert is_power_of_two(8)
    assert not is_power_of_two(15)
    assert is_power_of_two(16)
    assert is_power_of_two(32)