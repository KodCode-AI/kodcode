from solution import *

def test_can_make_beautiful():
    assert can_make_beautiful("аввава") == True
    assert can_make_beautiful("аиввава") == False
    assert can_make_beautiful("аивава") == False
    assert can_make_beautiful("aabbcc") == False
    assert can_make_beautiful("abcabc") == True
    assert can_make_beautiful("aa") == True
    assert can_make_beautiful("abcdefg") == False
    assert can_make_beautiful("aee") == True
    assert can_make_beautiful("eae") == True
    assert can_make_beautiful("ea") == True
    assert can_make_beautiful("aaee") == True