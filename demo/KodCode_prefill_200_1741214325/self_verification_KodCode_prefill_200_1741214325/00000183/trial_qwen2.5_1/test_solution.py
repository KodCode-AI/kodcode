from solution import *

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("12345") == "54321"