from solution import *

def test_rabin_karp_search():
    assert rabin_karp_search("ABCABCD", "ABCD") == 3
    assert rabin_karp_search("hello world", "world") == 6
    assert rabin_karp_search("a", "b") == -1
    assert rabin_karp_search("aaa", "aa") == 0
    assert rabin_karp_search("", "a") == -1
    assert rabin_karp_search("abc", "") == 0
    assert rabin_karp_search("abc", "a") == 0
    assert rabin_karp_search("abc", "abc") == 0
    # Test with large alphabet (lowercase and uppercase)
    assert rabin_karp_search("The quick brown fox", "QUICK") == 4

def test_rabin_karp_search_case_insensitive():
    # Ensure search is case insensitive
    assert rabin_karp_search("The quick Brown fox", "brown") == 14