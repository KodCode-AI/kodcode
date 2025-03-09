from solution import *

from solution import interleave_strings

def test_interleave_strings_equal_lengths():
    assert interleave_strings("ABCD", "XY") == "AXBYCD"
    assert interleave_strings("XY", "ABCD") == "XAYBCD"

def test_interleave_strings_with_masks():
    assert interleave_strings("AB", "XYZ") == "AXBYZ"

def test_interleave_strings_first_shorter():
    assert interleave_strings("AB", "XYZW") == "AXBYZ"

def test_interleave_strings_second_shorter():
    assert interleave_strings("XYZW", "AB") == "XAYBZ"

def test_interleave_strings_empty_strings():
    assert interleave_strings("", "") == ""
    assert interleave_strings("A", "") == "A"
    assert interleave_strings("", "A") == "A"
    assert interleave_strings("AB", "") == "AB"
    assert interleave_strings("", "XYZ") == "XYZ"