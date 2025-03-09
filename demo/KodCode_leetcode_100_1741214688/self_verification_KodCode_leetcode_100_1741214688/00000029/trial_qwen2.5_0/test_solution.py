from solution import *

import pytest

def test_longest_balanced_substring():
    assert longest_balanced_substring("1001", 1) == 4  # All characters can be changed to make the whole string balanced
    assert longest_balanced_substring("1001", 2) == 4  # Can change both '0's to '1's
    assert longest_balanced_substring("0011", 0) == 2  # No flips, longest balanced substring is "00" or "11"
    assert longest_balanced_substring("1100011", 2) == 7  # Can flip '0' at index 4 and '0' at index 6 to get "1101111"
    assert longest_balanced_substring("0001111", 2) == 6  # Can flip '1' at indices 3 and 4 to get "0000000"
    assert longest_balanced_substring("1110111000", 3) == 8  # Can flip '1' at indices 3, 4, and 5 to get "1100111000"