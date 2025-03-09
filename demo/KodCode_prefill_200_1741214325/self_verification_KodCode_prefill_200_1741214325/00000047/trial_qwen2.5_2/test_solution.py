from solution import *

import pytest

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_palindrome_odd_length():
    assert is_palindrome("abccba") == True

def test_is_palindrome_palindrome_even_length():
    assert is_palindrome("racecar") == True

def test_is_palindrome_not_palindrome_odd_length():
    assert is_palindrome("hello") == False

def test_is_palindrome_not_palindrome_even_length():
    assert is_palindrome("hellothere") == False

def test_is_palindrome_with_spaces():
    assert is_palindrome("a man a plan a canal panama") == True

def test_is_palindrome_with_special_characters():
    assert is_palindrome("A man, a plan, a canal, Panama!") == True

def test_is_palindrome_case_sensitive():
    assert is_palindrome("Alice Bob, Bob Alice") == False