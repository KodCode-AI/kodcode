from solution import *

import pytest

def test_bin_to_octal():
    # Test cases
    assert bin_to_octal("1111") == "17"
    assert bin_to_octal("101010101010011") == "52523"
    assert bin_to_octal("00011000") == "30"
    assert bin_to_octal("100") == "4"
    assert bin_to_octal("111") == "7"
    assert bin_to_octal("110010000000000000000000") == "407000"
    assert bin_to_octal("") == ""

def test_bin_to_octal_errors():
    with pytest.raises(ValueError):
        bin_to_octal("a-1")
    with pytest.raises(ValueError):
        bin_to_octal("1020")

def test_bin_to_octal_empty_string():
    assert bin_to_octal("") == ""