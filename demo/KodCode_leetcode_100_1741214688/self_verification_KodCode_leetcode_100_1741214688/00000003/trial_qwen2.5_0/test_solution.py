from solution import *

def test_smallest_string():
    assert smallest_string("dcab") == "abcd", "Test case 1 failed"
    assert smallest_string("baaca") == "aaabc", "Test case 2 failed"
    assert smallest_string("abcd") == "abcd", "Test case 3 failed"
    assert smallest_string("cba") == "abc", "Test case 4 failed"
    assert smallest_string("a") == "a", "Test case 5 failed"