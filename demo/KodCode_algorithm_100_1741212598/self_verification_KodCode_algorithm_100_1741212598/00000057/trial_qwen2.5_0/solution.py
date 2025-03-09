import numpy as np
import cv2

def create_gaussian_kernel(size, sigma):
    """
    Creates a normalized Gaussian kernel of the given size and standard deviation.
    """
    half_size = (size - 1) // 2
    kernel = np.fromfunction(
        lambda x, y: (1 / (2 * np.pi * sigma**2)) * np.exp(
            -((x - half_size)**2 + (y - half_size)**2) / (2 * sigma**2)
        ),
        (size, size),
        dtype=float
    )
    kernel /= np.sum(kernel)  # Normalize the kernel
    return kernel

def apply_kernel(image, kernel):
    """
    Applies a normalized kernel to the image using cross-correlation.
    """
    kernel_size = kernel.shape[0]
    half_kernel_size = kernel_size // 2
    padded_image = np.pad(image, half_kernel_size, mode='constant')
    filtered_image = np.zeros_like(image, dtype=float)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            filtered_image[i, j] = np.sum(padded_image[i:i+kernel_size, j:j+kernel_size] * kernel)
    return filtered_image

def gaussian_filter(image, k_size, sigma):
    """
    Applies a Gaussian filter to the image using the given kernel size and standard deviation.
    """
    kernel = create_gaussian_kernel(k_size, sigma)
    return apply_kernel(image, kernel)