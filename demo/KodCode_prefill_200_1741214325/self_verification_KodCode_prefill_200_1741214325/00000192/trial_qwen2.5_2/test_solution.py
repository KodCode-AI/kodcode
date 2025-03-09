from solution import *

from solution import first_repeating_char

def test_first_repeating_char():
    assert first_repeating_char("programming") == 'r'
    assert first_repeating_char("python") == -1
    assert first_repeating_char("abacabad") == 'a'
    assert first_repeating_char("xyz") == -1
    assert first_repeating_char("aAAbcCddEe") == 'a'