from solution import *

from solution import minimal_string

def test_minimal_string_single_char():
    assert minimal_string("a") == "a"

def test_minimal_string_all_a():
    assert minimal_string("aaa") == "aaa"
    assert minimal_string("aaaa") == "aaaa"

def test_minimal_string_mixed():
    assert minimal_string("abca") == "aaabc"
    assert minimal_string("cbaa") == "aaaab"
    assert minimal_string("aaab") == "aaabb"
    assert minimal_string("cdaba") == "aaabcd"

def test_minimal_string_with_z():
    assert minimal_string("azbca") == "aaabc"
    assert minimal_string("zbcad") == "aaabc"
    assert minimal_string("cadzb") == "aaabc"
    assert minimal_string("zzbca") == "aaabc"