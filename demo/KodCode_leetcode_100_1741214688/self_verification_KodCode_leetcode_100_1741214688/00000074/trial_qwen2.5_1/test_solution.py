from solution import *

def test_form_smallest_palindrome():
    assert form_smallest_palindrome("aabb") == "abba"
    assert form_smallest_palindrome("abcd") == "abcd"
    assert form_smallest_palindrome("aabc") == "abac"
    assert form_smallest_palindrome("racecar") == "racecar"  # Already a palindrome
    assert form_smallest_palindrome("zidiveer") == "zidveeer"

def test_other_cases():
    assert form_smallest_palindrome("bbaa") == "abba"
    assert form_smallest_palindrome("edcba") == "abcde"
    assert form_smallest_palindrome("efgh") == "efgh"
    assert form_smallest_palindrome("zxcvbnm") == "zxcvbnm"
    assert form_smallest_palindrome("aaab") == "aabaa"