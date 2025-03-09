from solution import *

def test_max_length_balanced_substring():
    assert max_length_balanced_substring("aabbc", 2) == 5
    assert max_length_balanced_substring("abcabc", 3) == 5
    assert max_length_balanced_substring("cbccbcc<dim", 2) == 5
    assert max_length_balanced_substring("aaabb", 2) == 3
    assert max_length_balanced_substring("cccc", 1) == 4
    assert max_length_balanced_substring("cccaaa", 3) == 6
    assert max_length_balanced_substring("abababab", 2) == 4
    assert max_length_balanced_substring("abababab", 5) == 8

test_max_length_balanced_substring()