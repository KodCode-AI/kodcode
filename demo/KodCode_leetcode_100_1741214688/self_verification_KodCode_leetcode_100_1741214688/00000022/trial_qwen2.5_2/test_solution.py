from solution import *

from solution import longest_palindromic_substring, expand_around_center

def test_longest_palindromic_substring():
    assert longest_palindromic_substring("babad") == 3
    assert longest_palindromic_substring("cbbd") == 2
    assert longest_palindromic_substring("a") == 1
    assert longest_palindromic_substring("") == 0
    assert longest_palindromic_substring("racecar") == 7

def test_expand_around_center():
    assert expand_around_center("babad", 1, 1) == 3
    assert expand_around_center("babad", 0, 0) == 1
    assert expand_around_center("babad", 2, 2) == 3
    assert expand_around_center("babad", 3, 3) == 1
    assert expand_around_center("babad", 4, 4) == 1
    assert expand_around_center("cbbd", 1, 2) == 2
    assert expand_around_center("cbbd", 0, 1) == 1