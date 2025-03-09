from solution import *

from solution import capitalize_first_last_char

def test_capitalize_first_last_char():
    assert capitalize_first_last_char("hello") == "HeLlo"
    assert capitalize_first_last_char("a") == "A"
    assert capitalize_first_last_char("ab") == "Ab"

def test_special_characters():
    assert capitalize_first_last_char("!@#") == "!@#"
    assert capitalize_first_last_char("$") == "$"

def test_empty_string():
    assert capitalize_first_last_char("") == ""

def test_single_space_string():
    assert capitalize_first_last_char(" ") == "  "