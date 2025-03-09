from solution import *

def test_reverse_segment():
    assert reverse_segment("abcdeaa", 3) == "aebcd"
    assert reverse_segment("aabb", 2) == "aaab"
    assert reverse_segment("abracadabra", 3) == "aacaabrdrab"
    assert reverse_segment("abcd", 1) == "abcd"
    assert reverse_segment("aaa", 2) == "aaa"
    assert reverse_segment("a", 1) == "a"
    assert reverse_segment("b", 1) == "b"
    assert reverse_segment("babaa", 2) == "aabab"
    assert reverse_segment("abcdefa", 4) == "fbcdea"
    assert reverse_segment("xyz", 2) == "xyz"