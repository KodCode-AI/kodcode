from solution import *

from solution import lexicographically_smallest_string

def test_rotate_string_positive():
    assert rotate_string("abcde", 2) == "deabc"

def test_rotate_string_negative():
    assert rotate_string("abcde", -2) == "cdeab"

def test_lexicographically_smallest_string_positive():
    assert lexicographically_smallest_string("baaca", 3) == ("aaabc", 3)

def test_lexicographically_smallest_string_with_duplicates():
    assert lexicographically_smallest_string("bbzb", 2) == ("bzbb", 2)

def test_lexicographically_smallest_string_already_smallest():
    assert lexicographically_smallest_string("abcd", 4) == ("abcd", 1)

def test_lexicographically_smallest_string_single_char():
    assert lexicographically_smallest_string("a", 10) == ("a", 1)