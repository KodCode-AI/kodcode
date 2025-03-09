from solution import *

from solution import form_smallest_palindrome

def test_form_smallest_palindrome():
    assert form_smallest_palindrome("aabbcc", 3) == "abcabc"
    assert form_smallest_palindrome("abccba", 2) == "abccba"
    assert form_smallest_palindrome("abcdef", 2) == "abdcfe"
    assert form_smallest_palindrome("abcde", 0) == ""
    assert form_smallest_palindrome("abccba", 1) == "abccba"
    assert form_smallest_palindrome("aebcbda", 3) == "aabccba"
    assert form_smallest_palindrome("aebcbda", 4) == "aabbcda"