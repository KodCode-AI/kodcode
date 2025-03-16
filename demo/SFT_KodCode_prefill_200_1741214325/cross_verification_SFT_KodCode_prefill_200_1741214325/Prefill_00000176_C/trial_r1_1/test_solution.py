from solution import *

def test_min_deletions_to_palindrome():
    assert min_deletions_to_palindrome("abc") == 2
    assert min_deletions_to_palindrome("abcba") == 0
    assert min_deletions_to_palindrome("abcd") == 3
    assert min_deletions_to_palindrome("aaa") == 0
    assert min_deletions_to_palindrome("abccba") == 0
    assert min_deletions_to_palindrome("ababc") == 2
    assert min_deletions_to_palindrome("aba") == 0