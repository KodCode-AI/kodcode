from solution import *

def test_is_isomorphic():
    assert is_isomorphic("egg", "add") == True
    assert is_isomorphic("foo", "bar") == False
    assert is_isomorphic("paper", "title") == True
    assert is_isomorphic("badc", "baba") == False
    assert is_isomorphic("ab", "aa") == False
    assert is_isomorphic("", "") == True
    assert is_isomorphic("a", "a") == True
    assert is_isomorphic("aac", "yxy") == True
    assert is_isomorphic("aabb", "xyyx") == True
    assert is_isomorphic("aabb", "xyxy") == False