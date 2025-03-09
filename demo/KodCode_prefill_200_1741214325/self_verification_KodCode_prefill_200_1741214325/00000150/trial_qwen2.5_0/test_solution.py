from solution import *

def test_is_power_of_two():
    assert is_power_of_two(1) == True
    assert is_power_of_two(2) == True
    assert is_power_of_two(4) == True
    assert is_power_of_two(3) == False
    assert is_power_of_two(16) == True
    assert is_power_of_two(-2) == False
    assert is_power_of_two(0) == False
    assert is_power_of_two(1024) == True
    assert is_power_of_two(1023) == False