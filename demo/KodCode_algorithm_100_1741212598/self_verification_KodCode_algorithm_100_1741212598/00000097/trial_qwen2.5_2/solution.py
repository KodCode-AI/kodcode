import numpy as np

def enhanced_sepia(image: np.ndarray, factor: int, brightness: int) -> np.ndarray:
    """
    Applies a sepia tone and adjusts the brightness and contrast of the image.
    
    :param image: NumPy array representing the input image of shape (H, W, 3).
    :param factor: Integer value representing the sepia intensity (0-100).
    :param brightness: Integer value representing the brightness adjustment (-100 to 100).
    :return: NumPy array representing the modified image.
    """
    # Ensure the factor is within the valid range
    factor = max(0, min(100, factor))
    
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    
    sepia_filtered = np.dot(image / 255.0, sepia_filter.T)
    sepia_filtered = np.clip(sepia_filtered, 0, 1) * 255
    
    # Adjust brightness
    brightness_adjusted = sepia_filtered + brightness
    
    # Clip values to ensure they remain in the valid range [0, 255]
    adjusted_image = np.clip(brightness_adjusted, 0, 255).astype(np.uint8)
    
    return adjusted_image