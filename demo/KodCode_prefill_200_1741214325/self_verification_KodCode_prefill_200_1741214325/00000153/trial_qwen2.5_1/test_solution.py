from solution import *

from solution import count_vowels

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_count_vowels_no_vowels():
    assert count_vowels("bcxyz") == 0

def test_count_vowels_with_spaces():
    assert count_vowels("hello world") == 3

def test_count_vowels_with_diacritics():
    assert count_vowels("àéîôû") == 5

def test_count_vowels_with_mixed_cases():
    assert count_vowels("HEllo WORld") == 3