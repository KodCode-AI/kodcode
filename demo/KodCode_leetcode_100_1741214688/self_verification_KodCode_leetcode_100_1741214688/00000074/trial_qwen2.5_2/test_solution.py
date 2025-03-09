from solution import *

def test_form_smallest_palindrome():
    assert form_smallest_palindrome("egcfe") == "efcfe"
    assert form_smallest_palindrome("abcd") == "abba"
    assert form_smallest_palindrome("seven") == "seven"
    assert form_smallest_palindrome("aabbcc") == "abcbbc"
    assert form_smallest_palindrome("bbabcb") == "babcbb"
    assert form_smallest_palindrome("bcb") == "bcb"
    assert form_smallest_palindrome("aa") == "aa"
    assert form_smallest_palindrome("xyz") == "xyz"