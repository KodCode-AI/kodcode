from solution import *

def test_can_make_palindrome():
    assert can_make_palindrome("0000") == True
    assert can_make_palindrome("010010101") == True
    assert can_make_palindrome("0010100") == True
    assert can_make_palindrome("0101011") == False
    assert can_make_palindrome("11001011") == True
    assert can_make_palindrome("0001000") == True
    assert can_make_palindrome("1001001") == True
    assert can_make_palindrome("0110001") == False