from solution import *

from solution import modify_string

def test_modify_string_empty_string():
    assert modify_string("") == ""

def test_modify_string_single_character():
    assert modify_string("a") == "A"

def test_modify_string_all_uppercase():
    assert modify_string("abcd") == "ABcd"

def test_modify_string_all_lowercase():
    assert modify_string("abcde") == "Abccde"

def test_modify_string_mixed_case():
    assert modify_string("aBcDe") == "ABcDe"

def test_modify_string_with_spaces():
    assert modify_string("hello world") == "Hehello world"