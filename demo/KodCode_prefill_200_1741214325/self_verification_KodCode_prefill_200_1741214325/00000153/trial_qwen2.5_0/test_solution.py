from solution import *

from solution import count_vowels

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_one_vowel():
    assert count_vowels("Hello") == 2
    assert count_vowels("AEIOU") == 5

def test_count_vowels_with_consonants():
    assert count_vowels("This is a Test String") == 7
    assert count_vowels("Python Programming") == 4

def test_count_vowels_no_vowels():
    assert count_vowels("Rhythm") == 0
    assert count_vowels("bcdfghjkl") == 0

def test_count_vowels_mixed_case():
    assert count_vowels("BaNaNa") == 3
    assert count_vowels("HELLO") == 2
    assert count_vowels("Chapeau") == 2