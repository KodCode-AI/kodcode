from solution import *

from solution import enhanced_rabin_karp

def test_enhanced_rabin_karp():
    assert enhanced_rabin_karp("abc1abc12", "alskfjaldsabc1abc1abc12k23adsfabcabc", 256, 1000003) == [11, 21]
    assert enhanced_rabin_karp("ABABX", "ABABZABABYABABX", 256, 1000003) == [6]
    assert enhanced_rabin_karp("", "abc", 256, 1000003) == [0, 1, 2]
    assert enhanced_rabin_karp("a", "aaa", 256, 1000003) == [0, 1, 2]
    assert enhanced_rabin_karp("abcd", "abcde", 256, 1000003) == [0]
    assert enhanced_rabin_karp("xyz", "abcdef", 256, 1000003) == []
    assert enhanced_rabin_karp("a", "", 256, 1000003) == []
    assert enhanced_rabin_karp("", "", 256, 1000003) == []

test_enhanced_rabin_karp()