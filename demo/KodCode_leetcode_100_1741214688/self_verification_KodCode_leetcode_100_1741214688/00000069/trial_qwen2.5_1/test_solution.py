from solution import *

from solution import can_arrange_vowels_consonants

def test_can_arrange_vowels_consonants():
    assert can_arrange_vowels_consonants("*a[d") == False
    assert can_arrange_vowels_consonants("l*m*n") == False
    assert can_arrange_vowels_consonants("*&^") == True

def test_can_arrange_boundary_conditions():
    assert can_arrange_vowels_consonants("a") == False
    assert can_arrange_vowels_consonants("aa") == False

def test_can_arrange_random():
    assert can_arrange_vowels_consonants("aeiou") == False
    assert can_arrange_vowels_consonants("abcdefg") == False
    assert can_arrange_vowels_consonants("baca") == True
    assert can_arrange_vowels_consonants("ab") == False
    assert can_arrange_vowels_consonants("aeiouy") == True