from solution import *

import pytest

def test_bin_to_octal():
    # Test with a valid binary string
    assert bin_to_octal("1111") == "17"
    
    # Test with a larger binary string
    assert bin_to_octal("101010101010011") == "52523"
    
    # Test with an empty string
    assert bin_to_octal("") == ""
    
    # Test with a non-binary string (should raise ValueError)
    with pytest.raises(ValueError):
        bin_to_octal("a-1")
    
    # Test with a string that contains characters that are not '0' or '1'
    with pytest.raises(ValueError):
        bin_to_octal("1010x1010")

def test_optimization():
    # Test with a large binary string
    large_bin = '1' * 1000000  # A large number of 1s
    octal = bin_to_octal(large_bin)
    assert len(octal) == 333334  # Since 1000000 / 3 = 333333 with a remainder of 1, we expect 333334 digits in octal