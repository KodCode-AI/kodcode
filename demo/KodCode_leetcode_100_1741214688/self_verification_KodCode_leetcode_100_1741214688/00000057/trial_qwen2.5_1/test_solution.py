from solution import *

def test_smallest_by_reversing_substrings():
    assert smallest_by_reversing_substrings("cbaebabacd", 3) == "abacababc"
    assert smallest_by_reversing_substrings("aabc", 3) == "aacb"
    assert smallest_by_reversing_substrings("zxy", 3) == "xyz"
    assert smallest_by_reversing_substrings("abcd", 3) == "abdc"
    assert smallest_by_reversing_substrings("zzx", 3) == "zxx"
    assert smallest_by_reversing_substrings("cbabcabad", 3) == "abcabad"
    assert smallest_by_reversing_substrings("abcabc", 3) == "abcabc"