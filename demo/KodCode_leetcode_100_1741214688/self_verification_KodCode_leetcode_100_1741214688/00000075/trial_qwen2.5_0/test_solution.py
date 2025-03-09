from solution import *

from solution import make_smallest_lexicographical_string

def test_make_smallest_lexicographical_string():
    assert make_smallest_lexicographical_string("cba") == "abc"
    assert make_smallest_lexicographical_string("abcd") == "abcd"
    assert make_smallest_lexicographical_string("aabc") == "aaab"
    assert make_smallest_lexicographical_string("cbaabc") == "abcabc"
    assert make_smallest_lexicographical_string("cbabadcbbabbcbaba") == "aababacbbabc"