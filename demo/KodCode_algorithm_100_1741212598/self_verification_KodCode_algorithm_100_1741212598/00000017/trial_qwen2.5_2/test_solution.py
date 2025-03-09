from solution import *

``
import pytest

def test_find_pandigital_fibonacci():
    # Test the pre-defined value
    assert find_pandigital_fibonacci() == 329468

def test_check():
    # Test the check function
    assert check(123456789) == True
    assert check(987654321) == True
    assert check(12345) == False

def test_check1():
    # Test the check1 function
    assert check1(123456789) == True
    assert check1(987654321) == True
    assert check1(12345) == False