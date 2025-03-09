import requests
import shutil
import os

def download_and_save_apod(api_key: str, save_path: str) -> dict:
    """
    Fetches the "Astronomical Picture of the Day" (APOD) from NASA's APOD API and saves it to a specified directory.
    
    :param api_key: A valid NASA API key.
    :param save_path: A valid directory path where the APOD image will be saved.
    :return: A dictionary containing the APOD data.
    """
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Ensure the save directory exists
            os.makedirs(save_path, exist_ok=True)
            
            # Save the image to a file
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(os.path.join(save_path, "apod.jpg"), 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            
            # Parse the response JSON
            apod_data = response.json()
            return apod_data
        except (requests.exceptions.RequestException, IOError) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
            else:
                print("All attempts failed. Aborting.")
                return None