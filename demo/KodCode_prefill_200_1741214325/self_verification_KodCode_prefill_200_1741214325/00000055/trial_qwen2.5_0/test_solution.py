from solution import *

from solution import is_isomorphic

def test_isomorphic_strings():
    assert is_isomorphic("egg", "add") == True
    assert is_isomorphic("foo", "bar") == False
    assert is_isomorphic("paper", "title") == True
    assert is_isomorphic("badc", "baba") == False
    assert is_isomorphic("abab", "baba") == False
    assert is_isomorphic("ab", "aa") == False
    assert is_isomorphic("a", "b") == True
    assert is_isomorphic("aa", "bb") == True
    assert is_isomorphic("paper", "exas") == False