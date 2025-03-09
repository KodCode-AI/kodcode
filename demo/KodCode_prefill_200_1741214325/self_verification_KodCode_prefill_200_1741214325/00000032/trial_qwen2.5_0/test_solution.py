from solution import *

def test_is_binary_palindrome():
    assert is_binary_palindrome(1) == True  # binary is '1'
    assert is_binary_palindrome(2) == False # binary is '10'
    assert is_binary_palindrome(3) == True  # binary is '11'
    assert is_binary_palindrome(4) == False # binary is '100'
    assert is_binary_palindrome(5) == True  # binary is '101'
    assert is_binary_palindrome(6) == True  # binary is '110'
    assert is_binary_palindrome(7) == False # binary is '111'
    assert is_binary_palindrome(9) == True  # binary is '1001'