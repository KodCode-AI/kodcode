from solution import *

from solution import is_palindrome_number

def test_is_palindrome_number_positive():
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(1331) == True
    assert is_palindrome_number(12321) == True

def test_is_palindrome_number_negative():
    assert is_palindrome_number(-121) == False

def test_is_palindrome_number_zero():
    assert is_palindrome_number(0) == True

def test_is_palindrome_number_zero_padded():
    assert is_palindrome_number(1001) == True

def test_is_palindrome_number_single_digit():
    assert is_palindrome_number(7) == True

def test_is_palindrome_number_non_palindrome():
    assert is_palindrome_number(123) == False