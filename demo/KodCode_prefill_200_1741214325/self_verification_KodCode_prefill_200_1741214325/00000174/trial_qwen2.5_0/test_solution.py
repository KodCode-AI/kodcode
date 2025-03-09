from solution import *

from solution import longest_substring_two_distinct

def test_longest_substring_two_distinct():
    assert longest_substring_two_distinct("aabacbebebe") == 7
    assert longest_substring_two_distinct("abcabcabc") == 3
    assert longest_substring_two_distinct("abcd") == 4
    assert longest_substring_two_distinct("a") == 1
    assert longest_substring_two_distinct("") == 0
    assert longest_substring_two_distinct("aaabbaac") == 6
    assert longest_substring_two_distinct("zzzzzzz") == 1
    assert longest_substring_two_distinct("aabbxxbb") == 6