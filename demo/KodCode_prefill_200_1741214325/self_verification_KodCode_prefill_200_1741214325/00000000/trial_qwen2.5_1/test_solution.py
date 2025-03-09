from solution import *

from solution import remove_duplicates

def test_remove_duplicates_empty():
    assert remove_duplicates("") == ""

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates("abc") == "abc"

def test_remove_duplicates_with_duplicates():
    assert remove_duplicates("aabbcc") == "abc"
    assert remove_duplicates("aabbccddee") == "abcde"
    assert remove_duplicates("banana") == "ban"

def test_remove_duplicates_from_words():
    assert remove_duplicates("hello world") == "helo wrd"
    assert remove_duplicates("python programming") == "pyth o ramin"