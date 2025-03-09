from solution import *

from solution import smallest_string

def test_smallest_string_positive():
    assert smallest_string("cba") == "acb"
    assert smallest_string("baaca") == "aaabc"

def test_smallest_string_single_char():
    assert smallest_string("a") == "a"

def test_smallest_string_large_input():
    long_string = "z"*10000  # 10000 'z's
    assert smallest_string(long_string) == "z"*10000

def test_smallest_string_example1():
    assert smallest_string("ccaabaaca") == "aacaaabca"

def test_smallest_string_mixed_ascii():
    assert smallest_string("xyz") == "xyz"  # Already in the smallest lexicographical order