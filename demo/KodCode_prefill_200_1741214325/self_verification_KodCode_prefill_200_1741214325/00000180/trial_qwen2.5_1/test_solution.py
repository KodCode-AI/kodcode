from solution import *

from solution import has_consecutive_repeating_chars

def test_consecutive_repeating_chars():
    assert not has_consecutive_repeating_chars("abc")  # No consecutive repeating characters
    assert not has_consecutive_repeating_chars("aaab") # 'a' repeats but not separated by non-repeating chars
    assert has_consecutive_repeating_chars("aabb")    # 'a' and 'b' have consecutive repeats
    assert has_consecutive_repeating_chars("abbc")    # 'b' has a non-adjacent repeat
    assert has_consecutive_repeating_chars("cabbac")  # 'b' has a non-adjacent repeat
    assert not has_consecutive_repeating_chars("aaab") # Single segment of 3 'a's without non-repeating char