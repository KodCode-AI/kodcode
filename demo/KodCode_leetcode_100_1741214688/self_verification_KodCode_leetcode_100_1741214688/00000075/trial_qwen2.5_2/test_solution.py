from solution import *

def test_make_smallest_string():
    assert make_smallest_string("cba") == "abc"
    assert make_smallest_string("a") == "a"
    assert make_smallest_string("baa") == "aab"
    assert make_smallest_string("bdda") == "abcd"
    assert make_smallest_string("abcd") == "abcd"
    assert make_smallest_string("dacb") == "abdc"
    assert make_smallest_string("bdcaba") == "abcdba"