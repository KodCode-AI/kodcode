from solution import *

def test_reverse_segment():
    assert reverse_segment("abcdeaa", 3, 'a') == "aebcd"
    assert reverse_segment("aabcde", 2, 'a') == "aebcd"
    assert reverse_segment("abcd", 5, 'a') == "abcd"
    assert reverse_segment("ababa", 2, 'a') == "aaaba"
    assert reverse_segment("ababa", 5, 'b') == "baaba"
    assert reverse_segment("xyz", 1, 'a') == "xyz"
    assert reverse_segment("", 2, 'a') == ""
    assert reverse_segment("aaaaa", 3, 'a') == "aaaab"