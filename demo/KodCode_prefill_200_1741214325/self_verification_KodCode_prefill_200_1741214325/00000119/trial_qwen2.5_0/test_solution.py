from solution import *

from solution import replace_substring_with_spaces

def test_replace_substring_with_spaces_single_occurrence():
    assert replace_substring_with_spaces("hello world", "world", "Earth") == "hello Earth"

def test_replace_substring_with_spaces_multiple_occurrences():
    assert replace_substring_with_spaces("hello world world", "world", "Earth") == "hello Earth Earth"

def test_replace_substring_with_spaces_edge_case():
    assert replace_substring_with_spaces("world", "world", "Earth") == "Earth"

def test_replace_substring_with_spaces_surrounded_by_punctuation():
    assert replace_substring_with_spaces(",hello ,world,", "world", "Earth") == ",hello ,Earth,"

def test_replace_substring_with_spaces_no_occurrences():
    assert replace_substring_with_spaces("hello world", "universe", "Earth") == "hello world"

def test_replace_substring_with_spaces_no_spaces_around_substring():
    assert replace_substring_with_spaces("hello world", "world", "Earth") == "hello Earth"