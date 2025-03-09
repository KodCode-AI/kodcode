from solution import *

from solution import count_balanced_substrings

def test_count_balanced_substrings():
    assert count_balanced_substrings("abcabc", 2) == 3
    assert count_balanced_substrings("aaabbbccc", 3) == 1
    assert count_balanced_substrings("aabbcc", 2) == 3
    assert count_balanced_substrings("xyzz", 2) == 1
    assert count_balanced_substrings("zzzzz", 2) == 0

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])