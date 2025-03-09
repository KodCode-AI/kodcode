from solution import *

import pytest

def test_can_make_palindrome():
    assert can_make_palindrome("001101101") == False
    assert can_make_palindrome("010") == True
    assert can_make_palindrome("101") == True
    assert can_make_palindrome("111000111") == True
    assert can_make_palindrome("01001") == False
    assert can_make_palindrome("1010101") == True
    assert can_make_palindrome("10011001") == False
    assert can_make_palindrome("000") == True
    assert can_make_palindrome("1111111") == True
    assert can_make_palindrome("101101") == True