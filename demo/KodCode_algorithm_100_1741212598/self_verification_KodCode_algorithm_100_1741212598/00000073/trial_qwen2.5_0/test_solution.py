from solution import *

``
from solution import fetch_horoscope

def test_fetch_horoscope_valid_input():
    horoscope_text = fetch_horoscope(1, "today")
    assert horoscope_text.startswith("Your daily horoscope for today")

def test_fetch_horoscope_invalid_zodiac_sign():
    horoscope_text = fetch_horoscope(13, "today")
    assert horoscope_text == "Invalid zodiac sign."

def test_fetch_horoscope_invalid_day():
    horoscope_text = fetch_horoscope(1, "next week")
    assert horoscope_text == "Invalid day."

def test_fetch_horoscope_network_error_retry():
    # Simulate a network error by returning a status code other than 200
    with requests_mock.Mocker() as m:
        m.get("https://www.examplehoroscope.com/horoscope/1/today.html", status_code=404)
        horoscope_text = fetch_horoscope(1, "today")
        assert horoscope_text == "Failed to fetch the horoscope."