from solution import *

`  
import pytest

def test_enhanced_rabin_karp():
    assert enhanced_rabin_karp("abc1abc12", "alskfjaldsabc1abc1abc12k23adsfabcabc", 256, 1000003) == [11, 21]
    assert enhanced_rabin_karp("ABABX", "ABABZABABYABABX", 256, 1000003) == [6]
    assert enhanced_rabin_karp("", "abc", 256, 1000003) == []
    assert enhanced_rabin_karp("abc", "", 256, 1000003) == []
    assert enhanced_rabin_karp("a", "a", 256, 1000003) == [0]
    assert enhanced_rabin_karp("aa", "aaaaa", 256, 1000003) == [0, 1, 2, 3]
    assert enhanced_rabin_karp("test", "testtesttest", 256, 1000003) == [0, 4]

test_enhanced_rabin_karp()