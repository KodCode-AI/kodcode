from solution import *

from solution import count_palindromic_subsequences

def test_count_palindromic_subsequences():
    assert count_palindromic_subsequences("abc") == 3
    assert count_palindromic_subsequences("aaa") == 6
    assert count_palindromic_subsequences("aab") == 7
    assert count_palindromic_subsequences("odbcocdo") == 25
    assert count_palindromic_subsequences("a") == 1
    assert count_palindromic_subsequences("bb") == 3

def test_large_string():
    s = "abcdefghijklmnopqrstuvwxyz" * 1000
    assert 0 < count_palindromic_subsequences(s) <= 10**9 + 7