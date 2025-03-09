import numpy as np

def calculate_psnr(image1: np.ndarray, image2: np.ndarray) -> float:
    """
    Calculates the PSNR (Peak Signal-to-Noise Ratio) between two images.
    
    :param image1: First image as a NumPy array.
    :param image2: Second image as a NumPy array.
    :return: PSNR value in dB.
    """
    mse = np.mean((image1 - image2) ** 2)
    max_pixel_value = 255.0
    if mse == 0:
        return float('inf')
    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    return psnr