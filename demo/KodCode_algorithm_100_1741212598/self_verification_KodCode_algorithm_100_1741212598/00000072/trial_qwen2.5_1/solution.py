import numpy as np

def calculate_psnr(image1: np.ndarray, image2: np.ndarray) -> float:
    """
    Calculates the Peak Signal to Noise Ratio (PSNR) between two images.
    
    Parameters:
    image1 (np.ndarray): First image as a NumPy array.
    image2 (np.ndarray): Second image as a NumPy array.
    
    Returns:
    float: PSNR value in dB.
    """
    mse = np.mean((image1 - image2) ** 2)
    max_pixel = 255.0
    if mse == 0:
        return float('inf')
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr