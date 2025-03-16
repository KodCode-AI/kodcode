from solution import *

from solution import is_valid_palindrome

def test_is_valid_palindrome():
    assert is_valid_palindrome("A man, a plan, a canal: Panama") == True
    assert is_valid_palindrome("race a car") == False
    assert is_valid_palindrome("No lemon, no melon") == True
    assert is_valid_palindrome("") == True
    assert is_valid_palindrome(" ") == True
    assert is_valid_palindrome("a.") == True
    assert is_valid_palindrome("0P") == False
    assert is_valid_palindrome("Was it a car or a cat I saw?") == True