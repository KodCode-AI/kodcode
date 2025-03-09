from solution import *

import pytest

def test_longest_balanced_substring():
    assert longest_balanced_substring("abcbabc”) == 4
    assert longest_balanced_substring("aaabbbcc") == 6
    assert longest_balanced_substring("abcd") == 0
    assert longest_balanced_substring("aabbcc") == 6
    assert longest_balanced_substring("xxyyzzzz") == 4
    assert longest_balanced_substring("aabbcccdd") == 4
    assert longest_balanced_substring("bbaaac") == 0