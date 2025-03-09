from solution import *

import pytest

def test_count_balanced_substrings():
    assert count_balanced_substrings("abcabc", 2) == 3
    assert count_balanced_substrings("aaabbbccc", 3) == 1
    assert count_balanced_substrings("abababab", 2) == 8
    assert count_balanced_substrings("xyzxyz", 2) == 4
    assert count_balanced_substrings("aaaa", 1) == 4
    assert count_balanced_substrings("bana", 2) == 2
    assert count_balanced_substrings("abcabc", 4) == 0
    assert count_balanced_substrings("a", 1) == 1