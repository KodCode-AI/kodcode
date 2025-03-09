import numpy as np

def enhanced_sepia(image: np.ndarray, factor: int, brightness: int) -> np.ndarray:
    """
    Applies sepia tone and brightness/contrast adjustments to the input image.

    :param image: NumPy array representing the input image of shape (H, W, 3).
    :param factor: An integer representing the sepia effect intensity.
    :param brightness: An integer representing the brightness adjustment.
    :return: NumPy array representing the modified image.
    """
    # Ensure the factor is within the valid range
    factor = max(0, min(factor, 100))
    
    # Convert RGB to grayscale for the sepia calculation
    gray = np.dot(image[..., :3], [0.299, 0.587, 0.114])
    
    # Apply sepia effect based on the factor
    sepia_matrix = np.array([[0.393 + 0.607 * (factor / 100), 0.769 - 0.769 * (factor / 100), 0.189 - 0.189 * (factor / 100)],
                             [0.349 - 0.349 * (factor / 100), 0.686 + 0.314 * (factor / 100), 0.168 - 0.168 * (factor / 100)],
                             [0.272 - 0.272 * (factor / 100), 0.534 - 0.534 * (factor / 100), 0.131 + 0.869 * (factor / 100)]])
    
    # Apply sepia matrix and clip the values to avoid overflow
    sepia_image = np.clip(np.dot(gray[..., np.newaxis], sepia_matrix.T), 0, 255)
    
    # Normalize the sepia image to (0, 255) range
    sepia_image = (sepia_image / sepia_image.max() * 255).astype(np.uint8)
    
    # Apply brightness adjustment
    sepia_image += brightness
    
    # Ensure the brightness adjustment doesn't overflow
    sepia_image = np.clip(sepia_image, 0, 255)
    
    return sepia_image