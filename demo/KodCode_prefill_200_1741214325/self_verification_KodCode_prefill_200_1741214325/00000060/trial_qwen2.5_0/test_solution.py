from solution import *

def test_filter_strings_with_substring():
    assert filter_strings_with_substring(["apple", "banana", "grape", "berry"], "a") == ["apple", "banana", "berry"]
    assert filter_strings_with_substring(["hello", "world", "hi"], "h") == ["hello", "hi"]
    assert filter_strings_with_substring(["sun", "moon", "star"], "xyz") == []
    assert filter_strings_with_substring(["python", "java", "ruby"], "py") == ["python"]