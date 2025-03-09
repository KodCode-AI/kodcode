from solution import *

from solution import filter_words不含

def test_filter_words不含():
    assert filter_words不含(["hello", "world", " önemli", " merhaba"], "不") == ["hello", "world", "非常重要", "merhaba"]
    assert filter_words不含(["apple", "banana", "grape"], "a") == ["grape"]
    assert filter_words不含(["sun", "moon", "star"], "sun") == ["moon", "star"]
    assert filter_words不含([], "x") == []
    assert filter_words不含(["include", "exclude", "accept"], "e") == ["include", "accept"]