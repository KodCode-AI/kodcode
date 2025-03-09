from solution import *

from solution import longest_palindromic_substring

def test_longest_palindrome_single_character():
    assert longest_palindromic_substring("a") == 1

def test_longest_palindrome_short():
    assert longest_palindromic_substring("aba") == 3
    assert longest_palindromic_substring("ab") == 1

def test_longest_palindrome_middle_case():
    assert longest_palindromic_substring("saippuakauppias") == 16

def test_longest_palindrome_with_multiple_palindromes():
    assert longest_palindromic_substring("bananas") == 7
    assert longest_palindromic_substring("babad") == 3

def test_longest_palindrome_empty_string():
    assert longest_palindromic_substring("") == 0

def test_longest_palindrome_whole_string_palindrome():
    assert longest_palindromic_substring("aaaaa") == 5

def test_longest_palindrome_overlap():
    assert longest_palindromic_substring("abcba") == 5