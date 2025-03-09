import requests
from bs4 import BeautifulSoup
import time

def fetch_horoscope(zodiac_sign: int, day: str) -> str:
    # Validate inputs
    if zodiac_sign < 1 or zodiac_sign > 12:
        return "Invalid zodiac sign."
    valid_days = ["yesterday", "today", "tomorrow"]
    if day not in valid_days:
        return "Invalid day."
    
    # URL template
    base_url = "https://example.com/horoscope"
    url = f"{base_url}/{zodiac_sign}/{day}/full"
    
    # Retry mechanism
    for attempt in range(2):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract horoscope text (example extraction)
            horoscope_text = soup.find('div', {'class': 'horoscope-text'}).text.strip()
            return horoscope_text
        except requests.exceptions.RequestException as e:
            if attempt == 1:  # Only retry once
                return "Failed to fetch horoscope. Please try again later."
            time.sleep(5)  # Wait before retrying
    return "Failed to fetch horoscope. Please try again later."