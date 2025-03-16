from solution import *

from solution import is_isomorphic

def test_isomorphic_example1():
    assert is_isomorphic("egg", "add") == True

def test_isomorphic_example2():
    assert is_isomorphic("foo", "bar") == False

def test_isomorphic_example3():
    assert is_isomorphic("paper", "title") == True

def test_isomorphic_identical_strings():
    assert is_isomorphic("abc", "abc") == True

def test_isomorphic_empty_strings():
    assert is_isomorphic("", "") == True

def test_isomorphic_no_characters():
    assert is_isomorphic("a", "a") == True

def test_isomorphic_mismatched_characters():
    assert is_isomorphic("aabb", "ccdd") == True

def test_isomorphic_non_unique_replacement():
    assert is_isomorphic("ab", "aa") == False