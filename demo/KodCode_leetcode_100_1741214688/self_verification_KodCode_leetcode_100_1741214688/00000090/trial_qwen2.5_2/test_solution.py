from solution import *

from solution import count_balanced_substrings

def test_count_balanced_substrings():
    assert count_balanced_substrings('a') == 0
    assert count_balanced_substrings('aabcbaabc') == 4
    assert count_balanced_substrings('aa') == 1
    assert count_balanced_substrings('beeeecessary') == 3
    assert count_balanced_substrings('aebbcdeeeecba') == 6
    assert count_balanced_substrings('abcd') == 0