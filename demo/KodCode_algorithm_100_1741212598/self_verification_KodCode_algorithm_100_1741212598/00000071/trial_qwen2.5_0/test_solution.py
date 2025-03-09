from solution import *

import pytest
from unittest.mock import Mock, patch
from io import BytesIO
from PIL import Image
import requests

@pytest.fixture
def mock_response():
    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "date": "2023-09-01",
        "title": "Cool APOD",
        "url": "https://apod.nasa.gov/apod/image/2023/cool_apod.jpg"
    }
    response.raw = BytesIO(b"dummy image data")
    return response

@pytest.fixture
def mock_session():
    session = Mock()
    session.get.return_value = mock_response()
    return session

def test_download_and_save_apod(mock_session, tmp_path):
    api_key = "YOUR_API_KEY"
    save_path = tmp_path
    with patch("requests.Session", return_value=mock_session):
        data = download_and_save_apod(api_key, save_path)
    assert data == {
        "date": "2023-09-01",
        "title": "Cool APOD",
        "url": "https://apod.nasa.gov/apod/image/2023/cool_apod.jpg"
    }
    assert os.path.exists(os.path.join(save_path, "apod.jpg"))
    img = Image.open(os.path.join(save_path, "apod.jpg"))
    assert img.format == "JPEG"

def test_download_and_save_apod_with_error(mock_session):
    # Mock a failed request
    mock_session.get.side_effect = requests.exceptions.RequestException("Network error")
    with pytest.raises(requests.exceptions.RequestException):
        download_and_save_apod("invalid_api_key", "./")