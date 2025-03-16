from solution import *

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-4) == True
    assert is_even(-3) == False

def test_is_odd():
    assert is_even(1) == False
    assert is_even(-1) == False
    assert is_even(-5) == False