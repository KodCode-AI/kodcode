from solution import *

import numpy as np
import cv2
from solution import gaussian_filter

def test_gaussian_filter():
    # Generate a simple test image
    test_image = np.array([
        [0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0],
        [0, 4, 5, 6, 0],
        [0, 7, 8, 9, 0],
        [0, 0, 0, 0, 0]
    ], dtype=np.float32)
    
    # Apply the Gaussian filter
    filtered_image = gaussian_filter(test_image, 3, 1.0)
    
    # Expected result after applying Gaussian filter (approximate values)
    expected_filtered_image = np.array([
        [2.44, 3.44, 4.44, 3.44, 2.44],
        [4.16, 6.5, 9.0, 6.5, 4.16],
        [6.44, 9.0, 11.44, 9.0, 6.44],
        [4.16, 6.5, 9.0, 6.5, 4.16],
        [2.44, 3.44, 4.44, 3.44, 2.44]
    ], dtype=np.float32)
    
    # Calculate the difference between the expected and actual results
    diff = np.linalg.norm(filtered_image - expected_filtered_image)
    
    # Check if the difference is within an acceptable tolerance
    assert diff < 0.1, f"Expected filtered image to be close to expected_filtered_image, but got a difference of {diff}"

# Run the test
test_gaussian_filter()