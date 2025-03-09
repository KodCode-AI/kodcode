from solution import *

import pytest

def test_hex_to_bin_v2():
    # Positive tests
    assert hex_to_bin_v2("AC") == "10101100"
    assert hex_to_bin_v2("9A4") == "100110100100"
    assert hex_to_bin_v2("   12f   ") == "100101111"
    assert hex_to_bin_v2("FfFf") == "1111111111111111"
    assert hex_to_bin_v2("-fFfF") == "-1111111111111111"
    
    # Negative tests for invalid inputs
    with pytest.raises(ValueError, match="Invalid value was passed to the function"):
        hex_to_bin_v2("G1")
    with pytest.raises(ValueError, match="Invalid value was passed to the function"):
        hex_to_bin_v2("")
    with pytest.raises(ValueError, match="Invalid value was passed to the function"):
        hex_to_bin_v2("12g")
    with pytest.raises(ValueError, match="Invalid value was passed to the function"):
        hex_to_bin_v2("123456789012345678901234567890123456789012345678901234567890")