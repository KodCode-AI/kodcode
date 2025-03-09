from solution import *

from solution import remove_duplicates

def test_remove_duplicates_with_duplicates():
    assert remove_duplicates("programming") == "progamin"

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates("abcdef") == "abcdef"

def test_remove_duplicates_with_spaces():
    assert remove_duplicates("a b b c c d") == "a b c d"

def test_remove_duplicates_empty_string():
    assert remove_duplicates("") == ""

def test_remove_duplicates_with_special_characters():
    assert remove_duplicates("!!@@##$$%%^^&&**") == "!@#$%^&*"

def test_remove_duplicates_multiple_occurrences():
    assert remove_duplicates("taco cat") == "tac o "