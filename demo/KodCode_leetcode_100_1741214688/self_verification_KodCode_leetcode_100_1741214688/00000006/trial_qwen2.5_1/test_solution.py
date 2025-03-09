from solution import *

from solution import smallest_by_reversing_substrings

def test_smallest_by_reversing_substrings():
    assert smallest_by_reversing_substrings("cba") == "abc"
    assert smallest_by_reversing_substrings("aaba") == "aaab"
    assert smallest_by_reversing_substrings("cdadabcc") == "aadbcabc"
    assert smallest_by_reversing_substrings("abcd") == "abcd"
    assert smallest_by_reversing_substrings("baab") == "aabb"
    assert smallest_by_reversing_substrings("abcd") == "abcd"