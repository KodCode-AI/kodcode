from solution import *

import pytest

def test_form_smallest_palindrome():
    assert form_smallest_palindrome("egcfe") == "efcfe"
    assert form_smallest_palindrome("abcd") == "abcd"
    assert form_smallest_palindrome("edcba") == "abcde"
    assert form_smallest_palindrome("aabbcc") == "aabbc"
    assert form_smallest_palindrome("abcdedcba") == "abcdedcba"
    assert form_smallest_palindrome("abcde") == "abcde"
    assert form_smallest_palindrome("zzxyx") == "xyxzz"
    assert form_smallest_palindrome("x") == "x"
    assert form_smallest_palindrome("aab") == "aba"
    assert form_smallest_palindrome("baa") == "aba"
    assert form_smallest_palindrome("abcba") == "abcba"