from solution import *

def test_is_binary_palindrome():
    assert is_binary_palindrome(1) == True  # Binary: 1
    assert is_binary_palindrome(2) == False # Binary: 10
    assert is_binary_palindrome(3) == False # Binary: 11
    assert is_binary_palindrome(4) == True  # Binary: 100
    assert is_binary_palindrome(5) == False # Binary: 101
    assert is_binary_palindrome(6) == True  # Binary: 110
    assert is_binary_palindrome(7) == True  # Binary: 111
    assert is_binary_palindrome(13) == False # Binary: 1101
    assert is_binary_palindrome(15) == False # Binary: 1111
    assert is_binary_palindrome(19) == True  # Binary: 10011
    assert is_binary_palindrome(23) == True  # Binary: 10111
    assert is_binary_palindrome(29) == False # Binary: 11101
    assert is_binary_palindrome(31) == True  # Binary: 11111