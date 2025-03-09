from solution import *

from solution import can_arrange_string

def test_can_arrange_string():
    assert can_arrange_string("aabb") == True
    assert can_arrange_string("aaabc") == False
    assert can_arrange_string("aa") == False
    assert can_arrange_string("cdd") == True
    assert can_arrange_string("be") == False
    assert can_arrange_string("aabbc") == True
    assert can_arrange_string("ace") == True
    assert can_arrange_string("bda") == True
    assert can_arrange_string("aabbccddee") == True
    assert can_arrange_string("abc") == True
    assert can_arrange_string("aaaccc") == False

def test_odd_consonants():
    assert can_arrange_string("a") == False  # String length must be at least 2
    assert can_arrange_string("aa") == False  # At least one consonant is needed for odd positions

def test_vowel_parity():
    assert can_arrange_string("ad") == True
    assert can_arrange_string("ae") == False
    assert can_arrange_string("aeiou") == False

def test_consonant_parity():
    assert can_arrange_string("bc") == True
    assert can_arrange_string("bdc") == False