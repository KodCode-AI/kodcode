import requests
from bs4 import BeautifulSoup
import time

def fetch_horoscope(zodiac_sign: int, day: str) -> str:
    """
    Fetches the daily horoscope for a given zodiac sign and day.
    """
    if zodiac_sign < 1 or zodiac_sign > 12:
        return "Invalid zodiac sign. Please enter a value between 1 and 12."
    
    valid_days = ['yesterday', 'today', 'tomorrow']
    if day not in valid_days:
        return "Invalid day. Please choose from 'yesterday', 'today', or 'tomorrow'."
    
    url = f"https://www.examplehoroscope.com/horoscope-general-daily-{day}/{zodiac_sign}.html"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        time.sleep(2)
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException:
            return "Failed to fetch horoscope. Please try again later."
    
    soup = BeautifulSoup(response.content, 'html.parser')
    horoscope_text = soup.find('div', {'class': 'horoscope-text'}).text
    return horoscope_text

# Ensure to replace the URL and class name according to the actual website structure.