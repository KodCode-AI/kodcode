from solution import *

python
def test_find_pandigital_fibonacci():
    assert find_pandigital_fibonacci() == 329468

def test_check():
    assert check(123456789) is True
    assert check(987654321) is True
    assert check(12345) is False

def test_check1():
    assert check1(123456789) is True
    assert check1(987654321) is True
    assert check1(12345) is False
    assert check1(123456789987654321) is True
    assert check1(1234567890123456789) is True
    assert check1(1234567899999999999) is True
    assert check1(1234567899999999990) is False

def test_small_numbers():
    assert find_pandigital_fibonacci(1, 2, 2, 4, 8, 13, 21, 34, 55, 89) == 10  # Using smaller set of numbers for testing