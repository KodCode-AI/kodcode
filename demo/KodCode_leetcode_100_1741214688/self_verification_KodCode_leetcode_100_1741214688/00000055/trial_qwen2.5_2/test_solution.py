from solution import *

def test_smallest_string():
    assert smallest_string("cbaaaabc") == "aaaabca"
    assert smallest_string("bbb") == "b"
    assert smallest_string("abcde") == "abcde"
    assert smallest_string("zyxwvutsrq") == "q"
    assert smallest_string("a") == "a"
    assert smallest_string("aab") == "a"