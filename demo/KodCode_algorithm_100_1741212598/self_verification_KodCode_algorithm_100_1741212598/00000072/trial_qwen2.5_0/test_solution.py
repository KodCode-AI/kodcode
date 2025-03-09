from solution import *

import numpy as np

def test_psnr():
    # Test case 1: Identical images
    image1 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    image2 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    psnr = calculate_psnr(image1, image2)
    assert round(psnr, 2) == 100.0, f"Expected 100.0 dB, got {psnr} dB"

    # Test case 2: Different images
    image3 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    image4 = np.array([[129, 129, 129], [129, 129, 129]], dtype=np.uint8)
    psnr = calculate_psnr(image3, image4)
    assert round(psnr, 2) == 97.44, f"Expected 97.44 dB, got {psnr} dB"

    # Test case 3: Image with no error
    image5 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    image6 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    psnr = calculate_psnr(image5, image6)
    assert psnr == float('inf'), f"Expected infinity, got {psnr}"

    # Test case 4: Images with a larger difference
    image7 = np.array([[0, 0, 0], [0, 0, 0]], dtype=np.uint8)
    image8 = np.array([[255, 255, 255], [255, 255, 255]], dtype=np.uint8)
    psnr = calculate_psnr(image7, image8)
    assert round(psnr, 2) == 10.0, f"Expected 10.0 dB, got {psnr} dB"

    # Test case 5: From Wikipedia example (verify exact value for reference)
    image9 = np.array([[10, 10, 10], [10, 10, 10]], dtype=np.uint8)
    image10 = np.array([[10, 10, 10], [10, 8, 8]], dtype=np.uint8)
    psnr = calculate_psnr(image9, image10)
    assert round(psnr, 3) == 31.531, f"Expected 31.531 dB, got {psnr} dB"

test_psnr()