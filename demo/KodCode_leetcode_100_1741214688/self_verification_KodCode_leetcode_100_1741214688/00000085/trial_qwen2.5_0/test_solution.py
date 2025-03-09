from solution import *

def test_longest_balanced_substring():
    assert longest_balanced_substring("ababab") == 6
    assert longest_balanced_substring("aaabbb") == 6
    assert longest_balanced_substring("abac") == 4
    assert longest_balanced_substring("a") == 0
    assert longest_balanced_substring("aabbaa") == 4
    assert longest_balanced_substring("zzzzz") == 1

test_longest_balanced_substring()