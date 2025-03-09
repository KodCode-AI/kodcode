from solution import *

import pytest

def test_can_make_beautiful_palindrome():
    assert can_make_beautiful_palindrome("eaae") == True
    assert can_make_beautiful_palindrome("aceca") == True
    assert can_make_beautiful_palindrome("eee") == False
    assert can_make_beautiful_palindrome("aa") == True
    assert can_make_beautiful_palindrome("abc") == False
    assert can_make_beautiful_palindrome("automobile") == False
    assert can_make_beautiful_palindrome("aau") == True
    assert can_make_beautiful_palindrome("aaabc") == True
    assert can_make_beautiful_palindrome("aa") == True
    assert can_make_beautiful_palindrome("aab") == True
    assert can_make_beautiful_palindrome("aaabc") == True
    assert can_make_beautiful_palindrome("aaab") == True