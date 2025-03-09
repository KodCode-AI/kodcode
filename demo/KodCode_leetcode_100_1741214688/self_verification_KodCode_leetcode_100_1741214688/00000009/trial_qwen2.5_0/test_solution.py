from solution import *

from solution import max_balanced_substring_length

def test_max_balanced_substring_length():
    assert max_balanced_substring_length("aaabb", 3) == 3
    assert max_balanced_substring_length("ababbc", 2) == 5
    assert max_balanced_substring_length("cccc", 3) == 3
    assert max_balanced_substring_length("abcd", 1) == 1
    assert max_balanced_substring_length("abcd", 4) == 4
    assert max_balanced_substring_length("aabacbebebe", 3) == 7