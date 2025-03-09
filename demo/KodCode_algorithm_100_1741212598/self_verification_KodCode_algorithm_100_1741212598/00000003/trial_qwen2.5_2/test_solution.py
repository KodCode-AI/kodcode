from solution import *

def test_interleave_strings():
    assert interleave_strings("ABCD", "XY") == 'AXBYCD'
    assert interleave_strings("XY", "ABCD") == 'XAYBCD'
    assert interleave_strings("AB", "XYZ") == 'AXBYZ'
    assert interleave_strings("ABC", "") == 'ABC'
    assert interleave_strings("", "XYZ") == 'XYZ'
    assert interleave_strings("Hello", "World") == 'HWeolrllod'
    assert interleave_strings("short", "longerstring") == 'slhoorlngerstringt'