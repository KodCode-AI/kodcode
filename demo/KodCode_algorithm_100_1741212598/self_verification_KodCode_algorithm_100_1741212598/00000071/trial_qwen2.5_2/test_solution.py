from solution import *

import os
from unittest.mock import patch
from solution import download_and_save_apod

def test_download_and_save_apod():
    api_key = "YOUR_API_KEY"
    save_path = "./test_apod_images"
    data = download_and_save_apod(api_key, save_path)

    assert "url" in data
    assert "date" in data
    assert "title" in data
    assert "Explanation" in data
    
    image_path = os.path.join(save_path, f"apod_{data['date']}.jpg")
    assert os.path.exists(image_path)
    
    # Clean up
    os.remove(image_path)
    os.rmdir(save_path)

# Mock the APOD API response
def mock_apod_api_response(*args, **kwargs):
    class MockResponse:
        @staticmethod
        def json():
            return {
                "date": "2023-03-01",
                "title": "A beautiful cosmic sight",
                "url": "https://apod.nasa.gov/apod/image/2003/PC_Small.jpg",
                "hdurl": "https://apod.nasa.gov/apod/image/2003/PC_Small_HD.jpg"
            }
    return MockResponse()

@patch('requests.get', side_effect=mock_apod_api_response)
def test_download_and_save_apod_mocked(mock_get):
    api_key = "YOUR_API_KEY"
    save_path = "./test_apod_images"
    data = download_and_save_apod(api_key, save_path)

    assert "url" in data
    assert "date" in data
    assert "title" in data
    assert "Explanation" in data

    image_path = os.path.join(save_path, f"apod_{data['date']}.jpg")
    assert os.path.exists(image_path)
    
    # Clean up
    os.remove(image_path)
    os.rmdir(save_path)