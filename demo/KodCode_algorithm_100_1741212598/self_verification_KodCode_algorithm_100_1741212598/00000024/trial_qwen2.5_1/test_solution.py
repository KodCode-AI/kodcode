from solution import *

``
from solution import hex_to_bin_optimized

def test_hex_to_bin_optimized():
    assert hex_to_bin_optimized("AC") == "10101100"
    assert hex_to_bin_optimized("9A4") == "100110100100"
    assert hex_to_bin_optimized("   12f   ") == "100101111"
    assert hex_to_bin_optimized("FfFf") == "1111111111111111"
    assert hex_to_bin_optimized("-fFfF") == "-1111111111111111"
    try:
        hex_to_bin_optimized("F-f")
    except ValueError as e:
        assert str(e) == "Invalid value was passed to the function"
    try:
        hex_to_bin_optimized("")
    except ValueError as e:
        assert str(e) == "No value was passed to the function"