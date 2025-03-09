from solution import *

from solution import is_palindrome_number

def test_palindrome_number_positive():
    assert is_palindrome_number(121) == True

def test_palindrome_number_large():
    assert is_palindrome_number(12321) == True

def test_palindrome_number_edge_case():
    assert is_palindrome_number(1) == True

def test_palindrome_number_negative():
    assert is_palindrome_number(-121) == False

def test_palindrome_number_non_palindrome():
    assert is_palindrome_number(123) == False

def test_palindrome_number_zero():
    assert is_palindrome_number(0) == True