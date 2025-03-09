from solution import *

def test_first_repeating_char():
    assert first_repeating_char("programming") == 'r'
    assert first_repeating_char("abcdef") == -1
    assert first_repeating_char("aabbccddeeff") == 'a'
    assert first_repeating_char("abccba") == 'c'
    assert first_repeating_char("xyz") == -1
    assert first_repeating_char("") == -1
    assert first_repeating_char("aa") == 'a'

def test_first_repeating_char_with_numbers():
    assert first_repeating_char("12341") == '1'
    assert first_repeating_char("78907") == '7'
    assert first_repeating_char("123") == -1