from solution import *

def test_min_swaps_to_anagram():
    assert min_swaps_to_anagram("abc", "bca") == 0
    assert min_swaps_to_anagram("abcd", "cdab") == 2
    assert min_swaps_to_anagram("abcd", "dacb") == 4
    assert min_swaps_to_anagram("bananas", "bananas") == 0
    assert min_swaps_to_anagram("abc", "cba") == 1  # Only one swap needed
    assert min_swaps_to_anagram("abc", "def") == -1  # Different set of characters, not an anagram