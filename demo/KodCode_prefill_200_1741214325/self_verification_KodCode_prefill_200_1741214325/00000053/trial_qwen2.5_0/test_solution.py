from solution import *

import pytest
from solution import is_valid_palindrome

def test_is_valid_palindrome():
    assert is_valid_palindrome("A man, a plan, a canal: Panama") == True
    assert is_valid_palindrome("race a car") == False
    assert is_valid_palindrome(" ") == True
    assert is_valid_palindrome("No 'x' in Noxide") == True
    assert is_valid_palindrome("") == True
    assert is_valid_palindrome("12321") == True
    assert is_valid_palindrome("123a321") == True