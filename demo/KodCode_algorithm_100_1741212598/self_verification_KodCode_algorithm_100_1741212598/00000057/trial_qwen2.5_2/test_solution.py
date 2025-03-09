from solution import *

import numpy as np
import cv2
import matplotlib.pyplot as plt

def test_gaussian_filter(image_path, k_size, sigma):
    # Read the image as grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply the Gaussian filter
    filtered_image = gaussian_filter(img, k_size, sigma)
    
    # Display the original and filtered images
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Filtered Image')
    plt.axis('off')
    
    plt.show()

# Example test cases
test_gaussian_filter('test_images/sunflower.jpg', 5, 1.0)
test_gaussian_filter('test_images/camera.png', 3, 0.5)
test_gaussian_filter('test_images/peppers.png', 7, 2.0)