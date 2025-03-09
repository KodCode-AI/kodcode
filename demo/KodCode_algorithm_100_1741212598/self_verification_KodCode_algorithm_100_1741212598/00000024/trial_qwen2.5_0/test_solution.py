from solution import *

import pytest

def test_hex_to_bin_optimized():
    assert hex_to_bin_optimized("AC") == "10101100"
    assert hex_to_bin_optimized("9A4") == "100110100100"
    assert hex_to_bin_optimized("   12f   ") == "100101111"
    assert hex_to_bin_optimized("FfFf") == "1111111111111111"
    assert hex_to_bin_optimized("-fFfF") == "-1111111111111111"
    with pytest.raises(ValueError):
        hex_to_bin_optimized("F-f")
    with pytest.raises(ValueError):
        hex_to_bin_optimized("")

if __name__ == "__main__":
    pytest.main()