from solution import *

import pytest

def test_hex_to_bin_v2():
    # Test valid hexadecimal numbers
    assert hex_to_bin_v2("AC") == "10101100"
    assert hex_to_bin_v2("9A4") == "100110100100"
    assert hex_to_bin_v2("12f") == "100101111"
    assert hex_to_bin_v2("FF") == "11111111"
    assert hex_to_bin_v2("-FfF") == "-1111111111111111"

    # Test with leading/trailing whitespace
    assert hex_to_bin_v2("   12f   ") == "100101111"
    assert hex_to_bin_v2(" FfFf   ") == "1111111111111111"
    assert hex_to_bin_v2("- fFfF   ") == "-1111111111111111"

    # Test negative number correctly preserved
    assert hex_to_bin_v2("-fFfF") == "-1111111111111111"

    # Test invalid input
    with pytest.raises(ValueError, match="Invalid value was passed to the function"):
        hex_to_bin_v2("G1")

    with pytest.raises(ValueError, match="Invalid value was passed to the function"):
        hex_to_bin_v2("")

    with pytest.raises(ValueError, match="Invalid value was passed to the function"):
        hex_to_bin_v2("I234.")