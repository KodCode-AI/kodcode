from solution import *

from solution import is_palindrome

def test_is_palindrome_empty_string():
    assert is_palindrome("") is True

def test_is_palindrome_single_character():
    assert is_palindrome("a") is True

def test_is_palindrome_palindrome_string():
    assert is_palindrome("Racecar") is True

def test_is_palindrome_non_palindrome_string():
    assert is_palindrome("Hello") is False

def test_is_palindrome_mixed_case_string():
    assert is_palindrome("Madam, in Eden, I'm Adam") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True

def test_is_palindrome_with_special_characters():
    assert is_palindrome("A Toyota's a Toyota!") is True