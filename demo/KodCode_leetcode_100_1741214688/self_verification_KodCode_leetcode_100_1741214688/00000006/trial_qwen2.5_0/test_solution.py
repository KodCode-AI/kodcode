from solution import *

from solution import smallest_string

def test_smallest_string():
    assert smallest_string("dcde") == "dcced"
    assert smallest_string("abc") == "abc"
    assert smallest_string("fedacx") == "afedcx"
    assert smallest_string("abcd") == "abcd"
    assert smallest_string("cba") == "abc"