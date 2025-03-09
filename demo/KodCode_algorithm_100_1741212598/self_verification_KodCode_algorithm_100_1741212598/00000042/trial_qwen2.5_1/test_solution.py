from solution import *

`python
def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(1) == True
    assert is_palindrome(1234567890) == False

def test_sum_reverse():
    assert sum_reverse(123) == 444
    assert sum_reverse(109) == 1001
    assert sum_reverse(99) == 198
    assert sum_reverse(1234) == 5675

def test_count_lychrel():
    assert count_lychrel(10000) == 249
    assert count_lychrel(20000) == 472
    assert count_lychrel(5000) == 56
    assert count_lychrel(1000) == 12
    assert count_lychrel(1) == 0