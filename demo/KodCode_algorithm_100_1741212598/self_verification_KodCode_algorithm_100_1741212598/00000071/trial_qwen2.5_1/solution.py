import requests
import shutil
import os
from urllib.parse import urlparse

def download_and_save_apod(api_key: str, save_path: str) -> dict:
    """
    Downloads and saves the APOD (Astronomical Picture of the Day) image from NASA's APOD API to the specified save_path.
    
    Parameters:
    api_key (str): NASA APOD API key.
    save_path (str): Path where the image will be saved.
    
    Returns:
    dict: APOD data as a dictionary.
    """
    base_url = "https://api.nasa.gov/planetary/apod"
    headers = {"Accept": "application/json"}
    params = {"api_key": api_key}
    
    attempt = 1
    max_attempts = 3
    while attempt <= max_attempts:
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code == 200:
            apod_data = response.json()
            url = apod_data.get("hdurl", apod_data.get("url"))
            if url:
                image_url = url
                filename = os.path.basename(urlparse(image_url).path)
                image_path = os.path.join(save_path, filename)
                try:
                    os.makedirs(save_path, exist_ok=True)
                    with requests.get(image_url, stream=True) as r:
                        if r.status_code == 200:
                            with open(image_path, 'wb') as f:
                                shutil.copyfileobj(r.raw, f)
                                apod_data["path"] = image_path
                                return apod_data
                        else:
                            print(f"Failed to download image, received status code {r.status_code}.")
                except IOError as e:
                    print(f"File write error: {e}")
        else:
            print(f"Failed to fetch APOD data, received status code {response.status_code}.")
        
        attempt += 1
    
    return {}

# Example usage
api_key = "YOUR_API_KEY"
save_path = "./apod_images"
data = download_and_save_apod(api_key, save_path)
print(data)