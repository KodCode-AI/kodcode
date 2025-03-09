from solution import *

from solution import longest_substring_with_two_distinct_chars

def test_longest_substring_with_two_distinct_chars():
    assert longest_substring_with_two_distinct_chars("aabacbebebe") == 7
    assert longest_substring_with_two_distinct_chars("ccaabbb") == 5
    assert longest_substring_with_two_distinct_chars("abcabc") == 3
    assert longest_substring_with_two_distinct_chars("a") == 1
    assert longest_substring_with_two_distinct_chars("") == 0
    assert longest_substring_with_two_distinct_chars("bbbbbb") == 6
    assert longest_substring_with_two_distinct_chars("abaccc") == 5

# Testing edge cases
def test_longest_substring_with_two_distinct_chars_edge_cases():
    assert longest_substring_with_two_distinct_chars("a") == 1
    assert longest_substring_with_two_distinct_chars("") == 0
    assert longest_substring_with_two_distinct_chars("ab") == 2
    assert longest_substring_with_two_distinct_chars("aab") == 3
    assert longest_substring_with_two_distinct_chars("aabb") == 4
    assert longest_substring_with_two_distinct_chars("aabbcc") == 5
    assert longest_substring_with_two_distinct_chars("aabbcccc") == 6

# Testing strings with more than two distinct characters
def test_longest_substring_with_two_distinct_chars_more_than_two():
    assert longest_substring_with_two_distinct_chars("aabbccdde") == 6
    assert longest_substring_with_two_distinct_chars("abcdeff") == 5
    assert longest_substring_with_two_distinct_chars("abccdddddef") == 6
    assert longest_substring_with_two_distinct_chars("abcde") == 2