from solution import *

from solution import count_balanced_substrings

def test_count_balanced_substrings_single_vowel():
    assert count_balanced_substrings("aa") == 0

def test_count_balanced_substrings_consonant_intermixed():
    assert count_balanced_substrings("bcdf") == 0
    assert count_balanced_substrings("cfcfbgbgaac") == 6

def test_count_balanced_substrings_mixed():
    assert count_balanced_substrings("beaead") == 5
    assert count_balanced_substrings("aabbacbaee") == 9

def test_count_balanced_substrings_all_vowel():
    assert count_balanced_substrings("aaaaa") == 10

def test_count_balanced_substrings_all_consonant():
    assert count_balanced_substrings("bbbb") == 0

def test_count_balanced_substrings_balanced_substring():
    assert count_balanced_substrings("aeiou") == 5