from solution import *

from solution import longest_alphabetic_substring

def test_longest_alphabetic_substring():
    assert longest_alphabetic_substring("abcbdefg") == 7
    assert longest_alphabetic_substring("vgc") == 3
    assert longest_alphabetic_substring("abc") == 3
    assert longest_alphabetic_substring("abczxyz") == 5
    assert longest_alphabetic_substring("a") == 1
    assert longest_alphabetic_substring("abcd") == 4
    assert longest_alphabetic_substring("az") == 2
    assert longest_alphabetic_substring("azc") == 3