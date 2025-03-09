from solution import *

def test_beautiful_substrings():
    assert beautiful_substrings("abcabb") == 6
    assert beautiful_substrings("zzz") == 3
    assert beautiful_substrings("aaab") == 2
    assert beautiful_substrings("pqrstuv") == 0