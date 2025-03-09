from solution import *

from solution import is_palindrome, sum_reverse, count_lychrel

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(9) == True
    assert is_palindrome(0) == True

def test_sum_reverse():
    assert sum_reverse(47) == 107 # 47 + 74
    assert sum_reverse(349) == 1343 # 349 + 943
    assert sum_reverse(12345) == 16786 # 12345 + 54321

def test_count_lychrel():
    assert count_lychrel(10000) == 249
    assert count_lychrel(2000) == 113
    assert count_lychrel(1000) == 87
    assert count_lychrel(100000) == 2496

def test_edge_cases():
    assert count_lychrel(1) == 0
    assert count_lychrel(2) == 1
    assert count_lychrel(10) == 2