from solution import *

from solution import convert_currency_multiple

def test_convert_currency_multiple_valid_input():
    result = convert_currency_multiple("your_api_key", "USD", "INR", [1.0, 2.5, 3.0])
    assert result == "1.0: 1.0 74.65 INR, 2.5: 2.5 186.63 INR, 3.0: 3.0 223.98 INR"

def test_convert_currency_multiple_empty_input():
    result = convert_currency_multiple("your_api_key", "USD", "INR", [])
    assert result == "No amounts provided."

def test_convert_currency_multiple_invalid_currencies():
    result = convert_currency_multiple("your_api_key", "USD1", "INR2", [1.0, 2.5, 3.0])
    assert result == "Invalid currency codes provided."

def test_convert_currency_multiple_invalid_amounts():
    result = convert_currency_multiple("your_api_key", "USD", "INR", [1, 2.5, "three"])
    assert result == "Invalid amount values."