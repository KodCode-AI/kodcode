import numpy as np

def gaussian_filter(image, k_size, sigma):
    """
    Applies a Gaussian filter to the input grayscale image.

    Parameters:
    image (np.ndarray): Input grayscale image as a 2D NumPy array.
    k_size (int): Size of the kernel. Must be an odd integer.
    sigma (float): Standard deviation for Gaussian kernel.

    Returns:
    np.ndarray: Filtered image as a 2D NumPy array.
    """
    if k_size % 2 == 0:
        raise ValueError("Kernel size must be an odd integer")

    half_size = k_size // 2
    k = np.fromfunction(lambda x, y: 1 / (2 * np.pi * sigma**2) * np.exp(-((x - half_size)**2 + (y - half_size)**2) / (2 * sigma**2)), (k_size, k_size))
    k /= k.sum()

    filtered_image = np.zeros_like(image, dtype=float)

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            # Determine the kernel boundaries within the image
            start_x = max(0, x - half_size)
            end_x = min(image.shape[0], x + half_size + 1)
            start_y = max(0, y - half_size)
            end_y = min(image.shape[1], y + half_size + 1)

            # Extract the effective kernel and the corresponding image region
            kernel_region = k[(start_x - x + half_size):(end_x - x + half_size), (start_y - y + half_size):(end_y - y + half_size)]
            image_region = image[start_x:end_x, start_y:end_y]

            # Compute the filtered value
            filtered_image[x, y] = np.sum(image_region * kernel_region)

    return filtered_image