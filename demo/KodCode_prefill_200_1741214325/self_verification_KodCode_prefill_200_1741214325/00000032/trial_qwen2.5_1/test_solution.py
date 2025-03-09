from solution import *

def test_is_binary_palindrome():
    assert is_binary_palindrome(9) == True  # 9 in binary is 1001
    assert is_binary_palindrome(4) == False  # 4 in binary is 100
    assert is_binary_palindrome(1) == True  # 1 in binary is 1
    assert is_binary_palindrome(2) == False  # 2 in binary is 10
    assert is_binary_palindrome(3) == True  # 3 in binary is 11
    assert is_binary_palindrome(7) == True  # 7 in binary is 111
    assert is_binary_palindrome(13) == True  # 13 in binary is 1101
    assert is_binary_palindrome(23) == False  # 23 in binary is 10111