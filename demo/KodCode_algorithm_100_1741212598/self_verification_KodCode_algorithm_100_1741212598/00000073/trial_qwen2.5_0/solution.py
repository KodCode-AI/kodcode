import requests
from bs4 import BeautifulSoup

def fetch_horoscope(zodiac_sign: int, day: str) -> str:
    """
    Fetches the daily horoscope for the given zodiac sign and day.
    
    :param zodiac_sign: An integer representing the zodiac sign (1 for Aries, 2 for Taurus, ..., 12 for Pisces).
    :param day: A string representing the day for which the horoscope is requested (e.g., "yesterday", "today", "tomorrow").
    :return: The horoscope text as a string.
    """
    if zodiac_sign not in range(1, 13):
        return "Invalid zodiac sign."
    if day not in ["yesterday", "today", "tomorrow"]:
        return "Invalid day."

    url = f"https://www.examplehoroscope.com/horoscope/{zodiac_sign}/{day}.html"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException:
            return "Failed to fetch the horoscope."

    soup = BeautifulSoup(response.text, 'html.parser')
    horoscope_text = soup.find('div', class_='horoscope-text').get_text()
    return horoscope_text.strip()

# Example usage
print(fetch_horoscope(1, "today"))
print(fetch_horoscope(13, "today"))
print(fetch_horoscope(1, "next week"))