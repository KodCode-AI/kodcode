from solution import *

from solution import smallest_by_reversing_substrings

def test_smallest_by_reversing_substrings():
    assert smallest_by_reversing_substrings("cba") == "abc"
    assert smallest_by_reversing_substrings("aefba") == "aabbf"
    assert smallest_by_reversing_substrings("dbba") == "baab"
    assert smallest_by_reversing_substrings("abcd") == "abcd"
    assert smallest_by_reversing_substrings("cbaebababcc") == "abacabcbb"
    assert smallest_by_reversing_substrings("leetcode") == "cdelotee"