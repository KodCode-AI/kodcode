from solution import *

from solution import is_even

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False

def test_is_odd():
    assert is_even(3) is False
    assert is_even(-1) is False