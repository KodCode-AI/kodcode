import numpy as np

def calculate_psnr(image1: np.ndarray, image2: np.ndarray) -> float:
    """
    Calculates the Peak Signal-to-Noise Ratio (PSNR) between two images.
    
    :param image1: First image (grayscale, uint8)
    :param image2: Second image (grayscale, uint8)
    :return: PSNR value in dB
    """
    if image1.shape != image2.shape:
        raise ValueError("Image shapes do not match")
    
    height, width = image1.shape
    mse = np.mean((image1 - image2) ** 2)
    if mse == 0:
        return float('inf')  # Indicates perfect match
    
    max_pixel_value = 255.0
    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    return psnr