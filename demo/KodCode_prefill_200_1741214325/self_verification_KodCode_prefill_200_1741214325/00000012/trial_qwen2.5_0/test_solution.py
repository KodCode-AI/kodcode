from solution import *

def test_convert_chars_to_uppercase():
    assert convert_chars_to_uppercase("") == ""
    assert convert_chars_to_uppercase("a") == "A"
    assert convert_chars_to_uppercase("abc") == "Abc"
    assert convert_chars_to_uppercase("abcd") == "Abcd"
    assert convert_chars_to_uppercase("aBcD") == "ABcD"
    assert convert_chars_to_uppercase("hello") == "Hhello"
    assert convert_chars_to_uppercase("WORLD") == "WWORLD"