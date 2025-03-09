from solution import *

def test_smallest_string():
    assert smallest_string("cba") == "abc"
    assert smallest_string("baaca") == "aaabc"
    assert smallest_string("bdda") == "addb"
    assert smallest_string("zyx") == "xyz"
    assert smallest_string("a") == "a"