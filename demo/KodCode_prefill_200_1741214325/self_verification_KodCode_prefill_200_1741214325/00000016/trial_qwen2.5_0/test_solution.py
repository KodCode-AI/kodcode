from solution import *

from solution import count_chars_digits_special

def test_count_chars_digits_special():
    assert count_chars_digits_special("Hello, World! 123") == (10, 3, 3)
    assert count_chars_digits_special("1234567890!@#$%^&*()") == (22, 10, 12)
    assert count_chars_digits_special("AaBbCc123! ") == (6, 3, 2)
    assert count_chars_digits_special("") == (0, 0, 0)