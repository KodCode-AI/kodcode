from solution import *

def test_smallest_string():
    assert smallest_string("cbaaaabc") == "aaaabca"
    assert smallest_string("bbbbbb") == "bb"
    assert smallest_string("abcd") == "a"
    assert smallest_string("aaabbbccc") == "abc"
    assert smallest_string("zzzzz") == "z"
    assert smallest_string("aazbzbz") == "aaabz"
    assert smallest_string("abbaabba") == "aaa"
    assert smallest_string("zzzzyyyxx") == "xyz"