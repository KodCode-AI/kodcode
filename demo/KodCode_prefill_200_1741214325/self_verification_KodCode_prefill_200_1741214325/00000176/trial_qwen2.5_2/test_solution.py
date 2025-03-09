from solution import *

from solution import min_deletions_to_palindrome

def test_min_deletions_to_palindrome():
    assert min_deletions_to_palindrome("abdbca") == 1
    assert min_deletions_to_palindrome("cddpd") == 2
    assert min_deletions_to_palindrome("pqr") == 2
    assert min_deletions_to_palindrome("aaa") == 0
    assert min_deletions_to_palindrome("abc") == 2
    assert min_deletions_to_palindrome("abca") == 1
    assert min_deletions_to_palindrome("abcda") == 1