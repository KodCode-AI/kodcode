from solution import *

from solution import find_weird_numbers, is_abundant, is_semiperfect

def test_is_abundant():
    assert is_abundant(12) == True
    assert is_abundant(20) == False
    assert is_abundant(24) == True

def test_is_semiperfect():
    assert is_semiperfect(6) == True
    assert is_semiperfect(8) == True
    assert is_semiperfect(12) == True
    assert is_semiperfect(18) == True
    assert is_semiperfect(20) == False

def test_find_weird_numbers():
    assert find_weird_numbers([69, 70, 71]) == [70]
    assert find_weird_numbers([12, 18, 20, 24, 25]) == [20, 24]
    assert find_weird_numbers([118, 4030, 5830, 5867]) == [4030]