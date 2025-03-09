from solution import *

def test_count_balanced_substrings():
    assert count_balanced_substrings("aebbcedee") == 3
    assert count_balanced_substrings("aaabbb") == 0
    assert count_balanced_substrings("aeiou") == 1
    assert count_balanced_substrings("accdedcba") == 3
    assert count_balanced_substrings("zxyz") == 1