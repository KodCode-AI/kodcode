from solution import *

from solution import first_uniq_char

def test_first_uniq_char_with_unique():
    assert first_uniq_char("leetcode") == 'l'

def test_first_uniq_char_with_no_uniques():
    assert first_uniq_char("aabbcc") == '_'

def test_first_uniq_char_with_multiple_uniques_returns_first():
    assert first_uniq_char("loveleetcode") == 'l'

def test_first_uniq_char_empty_string():
    assert first_uniq_char("") == '_'

def test_first_uniq_char_single_character():
    assert first_uniq_char("a") == 'a'