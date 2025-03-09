from solution import *

`
def test_count_chars():
    assert count_chars("HelloWorld123!") == (10, 3, 2)
    assert count_chars("") == (0, 0, 0)
    assert count_chars("1234567890") == (0, 10, 0)
    assert count_chars("!@#$%^&*()") == (10, 0, 10)
    assert count_chars("aAaA1234567890!@#$%^&*()") == (7, 10, 10)