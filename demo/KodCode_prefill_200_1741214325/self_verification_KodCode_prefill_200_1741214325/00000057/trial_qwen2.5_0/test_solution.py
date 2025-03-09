from solution import *

def test_count_uppercase_letters_empty_string():
    assert count_uppercase_letters("") == 0

def test_count_uppercase_letters_no_uppercase():
    assert count_uppercase_letters("hello world") == 0

def test_count_uppercase_letters_all_uppercase():
    assert count_uppercase_letters("HELLO WORLD") == 10

def test_count_uppercase_letters_mixed_case():
    assert count_uppercase_letters("HeLlO WoRlD") == 6