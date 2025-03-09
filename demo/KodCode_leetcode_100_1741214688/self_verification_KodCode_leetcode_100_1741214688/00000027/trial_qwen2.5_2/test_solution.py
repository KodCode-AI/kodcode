from solution import *

def test_count_substrings():
    assert count_substrings(["code", "decode", "coding"], "code") == 2
    assert count_substrings(["hello", "world", "python"], "o") == 3
    assert count_substrings(["ababa", "aba", "a", "b", "ba"], "aba") == 2
    assert count_substrings(["test", "exam", "sample"], "xyz") == 0
    assert count_substrings(["one", "two", "three", "four"], " ") == 3