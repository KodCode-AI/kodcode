from solution import *

import pytest

def test_longest_palindrome_length():
    assert longest_palindrome_length("babad") == 3
    assert longest_palindrome_length("cbbd") == 2
    assert longest_palindrome_length("a") == 1
    assert longest_palindrome_length("ac") == 1
    assert longest_palindrome_length("") == 0
    assert longest_palindrome_length("ccc") == 3
    assert longest_palindrome_length("banana") == 5
    assert longest_palindrome_length("racecar") == 7