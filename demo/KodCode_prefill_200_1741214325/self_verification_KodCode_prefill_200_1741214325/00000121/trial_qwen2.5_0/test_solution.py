from solution import *

def test_first_unique_char():
    assert first_unique_char("leetcode") == "l"
    assert first_unique_char("loveleetcode") == "v"
    assert first_unique_char("aabb") == '_'
    assert first_unique_char("preeeceeeeek") == 'r'
    assert first_unique_char("") == '_'
    assert first_unique_char("a") == "a"
    assert first_unique_char("aa") == '_'