from solution import *

def test_rabin_karp_search():
    assert rabin_karp_search("hello world", "world") == 6
    assert rabin_karp_search("a quick brown fox jumps over the lazy dog", "quick") == 2
    assert rabin_karp_search("repeat repeat repeat", "repeat") == 0
    assert rabin_karp_search("pythonythonpython", "python") == 6
    assert rabin_karp_search("does not contain the pattern", "pattern") == -1
    assert rabin_karp_search("a random string with a", "a") == 0
    assert rabin_karp_search("the quick brown fox", "the quick brown fox jumps over the lazy dog") == -1
    assert rabin_karp_search("a" * 10000, "a" * 100) == 0