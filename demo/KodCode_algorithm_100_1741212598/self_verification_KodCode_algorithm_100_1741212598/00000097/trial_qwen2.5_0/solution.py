import numpy as np

def enhanced_sepia(image: np.ndarray, factor: int, brightness: int) -> np.ndarray:
    """
    Applies a sepia tone to an image while adjusting its brightness and contrast.
    
    :param image: NumPy array of shape (H, W, 3) representing an image.
    :param factor: Integer representing the sepia effect intensity (0 to 100).
    :param brightness: Integer representing the brightness adjustment (-100 to 100).
    :return: Modified image as a NumPy array.
    """
    # Convert to float for easier manipulation
    image = image.astype(float)
    
    # Apply sepia effect
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_tone = np.dot(image, sepia_filter.T)
    
    # Apply factor to the sepia tone
    sepia_tone *= (factor / 100.0)
    
    # Clip values to keep them within [0, 255]
    sepia_tone = np.clip(sepia_tone, 0, 255)
    
    # Adjust brightness
    sepia_tone += brightness
    
    # Clip brightness values to maintain within [0, 255]
    sepia_tone = np.clip(sepia_tone, 0, 255)
    
    # Convert back to uint8
    sepia_tone = sepia_tone.astype(np.uint8)
    
    return sepia_tone