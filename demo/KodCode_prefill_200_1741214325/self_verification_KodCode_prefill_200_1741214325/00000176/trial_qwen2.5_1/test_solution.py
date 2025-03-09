from solution import *

def test_min_deletions_to_palindrome():
    assert min_deletions_to_palindrome("abca") == 1
    assert min_deletions_to_palindrome("abcba") == 0
    assert min_deletions_to_palindrome("abcde") == 4
    assert min_deletions_to_palindrome("aaa") == 0
    assert min_deletions_to_palindrome("abccba") == 0
    assert min_deletions_to_palindrome("abcddcba") == 1