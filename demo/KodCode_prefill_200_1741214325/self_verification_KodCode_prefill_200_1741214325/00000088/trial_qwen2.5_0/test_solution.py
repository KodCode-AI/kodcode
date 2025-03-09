from solution import *

def test_filter_words_notContaining_substring():
    assert filter_words_notContaining_substring(["hello", "world", "python", "alibaba", "cloud"], "o") == ["python", "cloud"]
    
def test_filter_words_notContaining_substring_empty_list():
    assert filter_words_notContaining_substring([], "x") == []
    
def test_filter_words_notContaining_substring_no_match():
    assert filter_words_notContaining_substring(["apple", "banana", "cherry"], "z") == ["apple", "banana", "cherry"]
    
def test_filter_words_notContaining_substring_with_substring():
    assert filter_words_notContaining_substring(["hello", "world", "homely", "como"], "lo") == ["hello", "homely"]