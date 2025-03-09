from solution import *

from solution import count_distinct_palindromic_subsequences

def test_count_distinct_palindromic_subsequences():
    assert count_distinct_palindromic_subsequences("abc") == 3  # "a", "b", "c"
    assert count_distinct_palindromic_subsequences("aaa") == 3  # "a", "a", "aaa"
    assert count_distinct_palindromic_subsequences("baa") == 3  # "a", "b", "aa"
    assert count_distinct_palindromic_subsequences("aabca") == 6  # "a", "b", "c", "aa", "aba", "aaca"
    assert count_distinct_palindromic_subsequences("aaaacaab") == 10
    assert count_distinct_palindromic_subsequences("aaaaa") == 5  # "a", "a", "aa", "aaa", "aaaa"
    assert count_distinct_palindromic_subsequences("abccba") == 11  # "a", "b", "c", "b", "c", "a", "bb", "cc", "bca", "bac", "abccba"