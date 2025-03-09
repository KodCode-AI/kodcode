from solution import *

import pytest
from pytest_mock import MockerFixture
from requests.models import Response

def mock_api_response(mocker, status_code=200, json_data=None):
    response = Response()
    response.status_code = status_code
    response.json = lambda: json_data if json_data else {}
    return mocker.patch('requests.post', return_value=response)

test_data = [
    (
        "your_api_key",
        "USD",
        "INR",
        [1.0, 2.5, 3.0],
        "1.0: 74.65 INR, 2.5: 186.63 INR, 3.0: 223.98 INR"
    ),
    (
        "wrong_api_key",
        "USD",
        "EUR",
        [1.0, 2.5, 3.0],
        "Error: The API call failed. Please check your internet connection or try again later."
    ),
    (
        "your_api_key",
        "INVALID_CURRENCY",
        "EUR",
        [1.0, 2.5, 3.0],
        "Error: Invalid response from the API."
    ),
    (
        "your_api_key",
        "USD",
        "EUR",
        [],
        "Error: The list of amounts is empty."
    ),
    (
        "your_api_key",
        "USD",
        "EUR",
        [1.0, 2.5, 3.0, 101.0],  # More than 100 elements
        "Error: The list of amounts is empty."
    ),
]

@pytest.mark.parametrize("api_key, from_currency, to_currency, amounts, expected_output", test_data)
def test_convert_currency_multiple(
    api_key: str,
    from_currency: str,
    to_currency: str,
    amounts: List[float],
    expected_output: str,
    mocker: MockerFixture
) -> None:
    mock_api_response(mocker)
    result = convert_currency_multiple(api_key, from_currency, to_currency, amounts)
    assert result == expected_output