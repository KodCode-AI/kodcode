from solution import *

def check(number: int) -> bool:
    return sorted(str(number)) == list('123456789')

def check1(number: int) -> bool:
    return sorted(str(number)) == list('123456789')[::-1]

def test_find_pandigital_fibonacci():
    assert find_pandigital_fibonacci() == 329468

def test_pandigital_properties():
    assert check(123456789)
    assert check1(987654321)
    assert not check(123456788)
    assert not check1(987654320)

def test_large_numbers():
    assert check(123456789123456789) == check(123456789123456789)
    assert check1(987654321987654321) == check1(987654321987654321)

def test_no_pandigital_in_range():
    assert find_pandigital_fibonacci() in range(1, 1000001)

def test_zero_case():
    assert find_pandigital_fibonacci(0) is None