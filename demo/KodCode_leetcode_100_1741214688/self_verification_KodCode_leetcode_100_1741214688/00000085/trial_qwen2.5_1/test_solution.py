from solution import *

def test_longest_balanced_substring():
    assert longest_balanced_substring("abba") == 2
    assert longest_balanced_substring("aabb") == 4
    assert longest_balanced_substring("abcabc") == 3
    assert longest_balanced_substring("aaabbb") == 2
    assert longest_balanced_substring("abcd") == 0
    assert longest_balanced_substring("aabbcc") == 6
    assert longest_balanced_substring("adbcabcda") == 5

def is_balanced(substring: str) -> bool:
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return all(value == char_count[char] for value in char_count.values())