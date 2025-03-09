from solution import *

def test_count_substring_occurrences():
    assert count_substring_occurrences("hellohellohello", "hello") == 3
    assert count_substring_occurrences("aaa", "a") == 3
    assert count_substring_occurrences("test", "nope") == 0
    assert count_substring_occurrences("", "a") == 0
    assert count_substring_occurrences("ababababa", "aba") == 2