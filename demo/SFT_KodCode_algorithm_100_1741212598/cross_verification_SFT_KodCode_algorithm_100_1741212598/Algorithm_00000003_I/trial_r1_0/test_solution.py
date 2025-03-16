from solution import *

from solution import interleave_strings

def test_interleave_strings():
    assert interleave_strings("ABCD", "XY") == "AXBYCD"
    assert interleave_strings("XY", "ABCD") == "XAYBCD"
    assert interleave_strings("AB", "XYZ") == "AXBYZ"
    assert interleave_strings("ABC", "") == "ABC"
    assert interleave_strings("", "XYZ") == "XYZ"
    assert interleave_strings("a" * 100000, "b" * 100000) == "ab" * 100000
    assert interleave_strings("a" * 100000, "") == "a" * 100000
    assert interleave_strings("", "b" * 100000) == "b" * 100000

def test_performance():
    from timeit import timeit
    # Check if the function can handle large input within 1 second
    large_input = "a" * 100000
    assert timeit(lambda: interleave_strings(large_input, large_input), number=1) < 1