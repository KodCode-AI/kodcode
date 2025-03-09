from solution import *

import pytest
from unittest.mock import patch, MagicMock

def test_convert_currency_multiple_positive():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "converted": [74.65, 186.63, 223.98]
        }
        mock_get.return_value = mock_response
        result = convert_currency_multiple("api_key", "USD", "INR", [1.0, 2.5, 3.0])
        assert result == "1.0: 74.65 INR, 2.5: 186.63 INR, 3.0: 223.98 INR"

def test_convert_currency_multiple_no_amounts():
    result = convert_currency_multiple("api_key", "USD", "INR", [])
    assert result == "Error: No amounts provided"

def test_convert_currency_multiple_api_failure():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        result = convert_currency_multiple("api_key", "USD", "INR", [1.0])
        assert result == "Error: API request failed with status 500"

def test_convert_currency_multiple_api_failure_with_error_message():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"error": "API failure"}
        mock_get.return_value = mock_response
        result = convert_currency_multiple("api_key", "USD", "INR", [1.0])
        assert result == "API failure"

def test_convert_currency_multiple_missing_package():
    with patch.dict('sys.modules', requests=None):
        result = convert_currency_multiple("api_key", "USD", "INR", [1.0])
        assert result == "Error: Missing required package 'requests'"

def test_convert_currency_multiple_invalid_currency_codes():
    result = convert_currency_multiple("api_key", "XXX", "YYY", [1.0])
    assert "Invalid currency code" in result