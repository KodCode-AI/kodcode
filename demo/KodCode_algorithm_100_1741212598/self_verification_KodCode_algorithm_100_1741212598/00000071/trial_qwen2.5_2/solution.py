import requests
import os
import shutil
from urllib3.exceptions import MaxRetryError, NewConnectionError

def download_and_save_apod(api_key: str, save_path: str) -> dict:
    """
    Fetches the APOD from NASA's APOD API and saves it to the specified directory.
    Implements error handling and retry mechanism.
    
    Args:
    api_key (str): NASA API key.
    save_path (str): Path where the image will be saved.
    
    Returns:
    dict: Dictionary containing APOD information.
    """
    base_url = "https://api.nasa.gov/planetary/apod"
    url = f"{base_url}?api_key={api_key}"
    
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            image_url = data["hdurl"] if "hdurl" in data else data["url"]
            
            image_data = requests.get(image_url, stream=True)
            image_data.raise_for_status()
            
            with open(os.path.join(save_path, f"apod_{data['date']}.jpg"), 'wb') as file:
                shutil.copyfileobj(image_data.raw, file)
                
            return data
        except (MaxRetryError, NewConnectionError) as e:
            print(f"Connection error on attempt {attempt + 1}: {e}")
            continue
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error on attempt {attempt + 1}: {e}")
            break
        except requests.exceptions.RequestException as e:
            print(f"Error on attempt {attempt + 1}: {e}")
            break
        except Exception as e:
            print(f"An unexpected error occurred on attempt {attempt + 1}: {e}")
            break
            
    return {}