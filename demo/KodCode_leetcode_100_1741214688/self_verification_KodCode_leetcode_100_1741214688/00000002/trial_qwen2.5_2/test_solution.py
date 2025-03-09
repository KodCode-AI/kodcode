from solution import *

from solution import count_beautiful_substrings

def test_count_beautiful_substrings():
    assert count_beautiful_substrings("abcabb") == 5
    assert count_beautiful_substrings("zzzz") == 2
    assert count_beautiful_substrings("aabbcc") == 6
    assert count_beautiful_substrings("abc") == 0
    assert count_beautiful_substrings("aaa") == 0
    assert count_beautiful_substrings("aabbaa") == 6