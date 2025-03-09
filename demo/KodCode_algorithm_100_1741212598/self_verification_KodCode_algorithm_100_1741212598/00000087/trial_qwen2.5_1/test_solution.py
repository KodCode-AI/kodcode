from solution import *

from solution import bin_to_octal

def test_bin_to_octal_with_small_bin_strings():
    assert bin_to_octal("1111") == "17"
    assert bin_to_octal("101010101010011") == "52523"

def test_bin_to_octal_with_empty_string():
    assert bin_to_octal("") == "0"

def test_bin_to_octal_with_non_binary_input():
    with pytest.raises(ValueError):
        bin_to_octal("a-1")

def test_bin_to_octal_with_large_bin_string():
    bin_str = '1' * 1000000  # Large binary string
    assert bin_to_octal(bin_str) == '3' * 333333  # Expected octal output

def test_bin_to_octal_with_repeated_padded_groups():
    assert bin_to_octal("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == '4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'