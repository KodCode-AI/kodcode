from solution import *

\nfrom solution import is_palindrome

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_palindrome_words():
    assert is_palindrome("racecar") == True
    assert is_palindrome("madam") == True

def test_is_palindrome_non_palindrome_words():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False

def test_is_palindrome_palindrome phrases():
    assert is_palindrome("A man a plan a canal Panama") == True

def test_is_palindrome_case_sensitive():
    assert is_palindrome("No lemon, no melon") == True

def test_is_palindrome_non_palindrome_phrases():
    assert is_palindrome("This is not a palindrome") == False
\n