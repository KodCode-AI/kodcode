from solution import *

import pytest

def test_count_beautiful_substrings():
    assert count_beautiful_substrings("abcabb") == 3  # "a", "bb", "abb" are beautiful
    assert count_beautiful_substrings("zzzz") == 3  # "z", "z", "zzz" are beautiful
    assert count_beautiful_substrings("abcd") == 0  # No beautiful substrings
    assert count_beautiful_substrings("xyzzxyzz") == 6  # "z", "z", "zzz", "xy", "yz", "zzz" are beautiful
    assert count_beautiful_substrings("abcdabcd") == 6  # "a", "b", "c", "d", "ab", "bc" are beautiful