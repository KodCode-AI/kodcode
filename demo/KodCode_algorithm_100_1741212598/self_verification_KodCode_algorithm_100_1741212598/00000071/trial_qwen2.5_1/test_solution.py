from solution import *

import os
from unittest.mock import patch, mock_open, MagicMock

def test_download_and_save_apod(mocker):
    api_key = "YOUR_API_KEY"
    save_path = "./apod_images"
    apod_data = {
        "hdurl": "https://apod.nasa.gov/apod/image/2303/CrabNebula_Hubble_2009_900.jpg",
        "title": "Crab Nebula",
        "date": "2023-03-22",
        "explanation": "A giant explosion...",
        "service_version": "1.0",
        "pi": "Astronomy Picture of the Day",
        "citation": "NASA/STScI/A. Loll/CXC/SAO",
        "url": "https://apod.nasa.gov/apod/image/2303/CrabNebula_Hubble_2009.jpg"
    }
    
    # Mock requests.get
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = apod_data
    mocker.patch('requests.get', return_value=mock_response)
    
    # Mock os.makedirs
    os.makedirs(save_path, exist_ok=True)
    
    # Mock open file for writing
    mock_open_file = mock_open()
    with patch('shutil.copyfileobj', return_value=None):
        with patch('builtins.open', mock_open_file):
            data = download_and_save_apod(api_key, save_path)
            assert data == apod_data

def test_error_handling(mocker):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mocker.patch('requests.get', return_value=mock_response)
    
    # Assert error is handled
    data = download_and_save_apod("invalid_api_key", "./apod_images")
    assert data is not None  # Still returns the error

def test_retry_mechanism(mocker):
    os.makedirs("./apod_images", exist_ok=True)
    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.side_effect = [requests.exceptions.RequestException] * 2 + [MagicMock(status_code=200)]
    apod_data = {
        "hdurl": "https://apod.nasa.gov/apod/image/2303/CrabNebula_Hubble_2009_900.jpg",
        "title": "Crab Nebula",
        "date": "2023-03-22",
    }
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = apod_data
    mock_requests_get.return_value = mock_response
    
    data = download_and_save_apod("valid_api_key", "./apod_images")
    assert data == apod_data