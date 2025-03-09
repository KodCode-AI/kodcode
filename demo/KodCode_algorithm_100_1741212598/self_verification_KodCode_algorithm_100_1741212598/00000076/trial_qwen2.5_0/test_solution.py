from solution import *

def test_hex_to_bin_v2():
    assert hex_to_bin_v2("AC") == "10101100"
    assert hex_to_bin_v2("9A4") == "100110100100"
    assert hex_to_bin_v2("   12f   ") == "100101111"
    assert hex_to_bin_v2("FfFf") == "1111111111111111"
    assert hex_to_bin_v2("-fFfF") == "-1111111111111111"
    
    # Test cases for invalid input
    try:
        hex_to_bin_v2("G1")
        assert False, "Expected ValueError for invalid hexadecimal input"
    except ValueError as e:
        assert str(e) == "Invalid value was passed to the function: G1"
    
    try:
        hex_to_bin_v2("")
        assert False, "Expected ValueError for empty string"
    except ValueError as e:
        assert str(e) == "No value was passed to the function"

# Run tests
test_hex_to_bin_v2()