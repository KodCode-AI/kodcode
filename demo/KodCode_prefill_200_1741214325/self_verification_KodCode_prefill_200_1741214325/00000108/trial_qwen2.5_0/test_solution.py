from solution import *

from solution import count_substring

def test_count_substring_empty_string():
    assert count_substring("", "test") == 0

def test_count_substring_no_occurrences():
    assert count_substring("hello world", "badchar") == 0

def test_count_substring_single_occurrence():
    assert count_substring("test test test", "test") == 3

def test_count_substring_multiple_occurrences():
    assert count_substring("bambambambam", "bam") == 4

def test_count_substring_substring_is_empty():
    assert count_substring("any string", "") == 0

def test_count_substring_substring_in_middle_of_word():
    assert count_substring("abracadabra", "a") == 5