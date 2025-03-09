from solution import *

from solution import fetch_horoscope

def test_fetch_horoscope_valid_input():
    assert "Your daily horoscope for today" in fetch_horoscope(1, "today")

def test_fetch_horoscope_invalid_zodiac_sign():
    assert "Invalid zodiac sign. Please enter a value between 1 and 12." == fetch_horoscope(13, "today")

def test_fetch_horoscope_invalid_day():
    assert "Invalid day. Please choose from 'yesterday', 'today', or 'tomorrow'." == fetch_horoscope(1, "next week")

def test_fetch_horoscope_network_error_retry_success():
    mock_response = 'Mock response text'
    response_mock = Mock()
    response_mock.status_code = 200
    with patch('requests.get', side_effect=[Exception('Failed'), response_mock]):
        assert "Mock response text" == fetch_horoscope(1, "today")

def test_fetch_horoscope_network_error_retry_failure():
    with patch('requests.get', side_effect=[Exception('Failed')] * 2):
        assert "Failed to fetch horoscope. Please try again later." == fetch_horoscope(1, "today")