from solution import *

import pytest
import requests
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
import time

def mock_requests_get(url, **kwargs):
    class MockResponse:
        def __init__(self, status_code, text):
            self.status_code = status_code
            self.text = text
        
        def raise_for_status(self):
            if self.status_code != 200:
                raise requests.exceptions.HTTPError
        
    if 'horoscope' in url:
        return MockResponse(200, '<div class="horoscope-text">Your daily horoscope for today</div>')
    elif 'invalid' in url:
        return MockResponse(404, '')
    else:
        return MockResponse(500, '')

@pytest.fixture(autouse=True)
def patch_requests_get():
    with patch('requests.get', side_effect=mock_requests_get) as mock_get:
        yield mock_get

def test_fetch_horoscope_valid_input():
    assert fetch_horoscope(1, "today") == "Your daily horoscope for today"

def test_fetch_horoscope_invalid_zodiac():
    assert fetch_horoscope(13, "today") == "Invalid zodiac sign."

def test_fetch_horoscope_invalid_day():
    assert fetch_horoscope(1, "next week") == "Invalid day."

def test_fetch_horoscope_network_error():
    with patch('requests.get', side_effect=requests.exceptions.RequestException):
        time.sleep = Mock()  # Prevent sleep during tests
        assert fetch_horoscope(1, "today") == "Failed to fetch horoscope. Please try again later."
    time.sleep = Mock()  # Cleanup

def test_fetch_horoscope_404_response():
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(404, '')
        assert fetch_horoscope(1, "today") == "Failed to fetch horoscope. Please try again later."

def test_fetch_horoscope_page_not_found():
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(200, '')
        assert fetch_horoscope(1, "today") == "Failed to fetch horoscope. Please try again later."