from solution import *

def test_count_substring_occurrences():
    assert count_substring_occurrences("Hello, hello, HELLO", "hello") == 3
    assert count_substring_occurrences("测试 测试 测试", "测试") == 3
    assert count_substring_occurrences("", "a") == 0
    assert count_substring_occurrences("aAaAaA", "Aa") == 3