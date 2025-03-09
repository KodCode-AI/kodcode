from solution import *

from solution import min_lexico_palindrome

def test_min_lexico_palindrome_with_k_zero():
    assert min_lexico_palindrome("abcb", 0) == "abcb"

def test_min_lexico_palindrome_possible():
    assert min_lexico_palindrome("bcb", 1) == "abc"

def test_min_lexico_palindrome_impossible():
    assert min_lexico_palindrome("bcb", 0) == ""

def test_min_lexico_palindrome_uneven_k():
    assert min_lexico_palindrome("aaab", 2) == "aaab"

def test_min_lexico_palindrome_is_palindrome():
    assert min_lexico_palindrome("madan氡丹mad", 5) == "madan氡丹mad"

def test_min_lexico_palindrome_positive_numbers():
    assert min_lexico_palindrome("aebcb", 2) == "aabc"

def test_min_lexico_palindrome_negative_numbers():
    assert min_lexico_palindrome("abcde", 5) == "abcde"