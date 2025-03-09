from solution import *

import pytest

def test_count_substring_occurrences():
    assert count_substring_occurrences("Hello, hello, HELLO!", "hello") == 3

def test_count_substring_occurrences_empty_string():
    assert count_substring_occurrences("", "test") == 0

def test_count_substring_occurrences_no_occurrence():
    assert count_substring_occurrences("abcABCABC", "xyz") == 0

def test_count_substring_occurrences_case_sensitivity():
    assert count_substring_occurrences("CaseSensitive CaseSensitive", "cASEsENSITIVE") == 2

def test_count_substring_occurrences_single_character():
    assert count_substring_occurrences("aAaAaA", "a") == 3
    assert count_substring_occurrences("aAaAaA", "A") == 3