import numpy as np
import cv2

def gaussian_filter(image, k_size, sigma):
    """
    Apply a Gaussian filter to the input grayscale image.
    """
    kernel = cv2.getGaussianKernel(k_size, sigma)
    kernel_2D = np.outer(kernel, kernel.transpose())
    kernel_2D /= kernel_2D.sum()
    
    filtered_image = np.zeros_like(image)
    pad_size = k_size // 2
    padded_image = np.pad(image, pad_size, mode='edge')
    
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            filtered_image[y, x] = (padded_image[y:y+k_size, x:x+k_size] * kernel_2D).sum()
    
    return filtered_image