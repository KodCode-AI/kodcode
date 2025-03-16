from solution import *

def test_string_to_ascii_list():
    assert string_to_ascii_list("AB") == [65, 66]
    assert string_to_ascii_list("Hello") == [72, 101, 108, 108, 111]
    assert string_to_ascii_list("") == []
    assert string_to_ascii_list("123") == [49, 50, 51]

def test_empty_string():
    assert string_to_ascii_list("") == []

def test_string_with_spaces():
    assert string_to_ascii_list("Hello World!") == [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]