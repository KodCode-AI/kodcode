from solution import *

from solution import count_vowels

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_count_vowels_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_count_vowels_mixed_string():
    assert count_vowels("Hello World!") == 3

def test_count_vowels_with_spaces():
    assert count_vowels("Quick Brown Fox Jumps Over The Lazy Dog") == 11