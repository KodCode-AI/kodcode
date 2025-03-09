from solution import *

from solution import smallest_string

def test_smallest_string():
    assert smallest_string("cbaaaabc") == "aaaabca"
    assert smallest_string("leetcode") == "aaaceeee"
    assert smallest_string("abc") == "a"
    assert smallest_string("bb") == "b"
    assert smallest_string("a") == "a"
    assert smallest_string("abccba") == "aacca"
    assert smallest_string("zxy") == "xyz"
    assert smallest_string("xyzzyx") == "xyyxy"