from solution import *

import numpy as np
import cv2
import pytest
import matplotlib.pyplot as plt

def create_gaussian_kernel_test():
    kernel = create_gaussian_kernel(3, 1.0)
    expected_kernel = np.array([[0.09473428, 0.12364155, 0.09473428],
                                [0.12364155, 0.16266196, 0.12364155],
                                [0.09473428, 0.12364155, 0.09473428]])
    np.testing.assert_almost_equal(kernel, expected_kernel, decimal=6)

def apply_kernel_test():
    image = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]], dtype=float)
    kernel = np.array([[0.09, 0.11, 0.09],
                       [0.11, 0.12, 0.11],
                       [0.09, 0.11, 0.09]])
    filtered_image = apply_kernel(image, kernel)
    expected_filtered_image = np.array([
        [3.1400000000000007, 4.220000000000001, 4.4400000000000014],
        [6.819999999999999, 7.629999999999999, 8.839999999999998],
        [7.520000000000001, 8.600000000000002, 9.440000000000002]
    ])
    np.testing.assert_almost_equal(filtered_image, expected_filtered_image, decimal=6)

def test_gaussian_filter(image_path, k_size, sigma):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    filtered_img = gaussian_filter(img, k_size, sigma)
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(filtered_img, cmap='gray')
    plt.title('Filtered Image')
    plt.axis('off')
    
    plt.show()

# Test the Gaussian filter on an example image
test_gaussian_filter('path_to_image.jpg', 5, 1.0)