from solution import *

import numpy as np
import pytest

def test_psnr():
    # Test case 1: Identical images
    image1 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    image2 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    psnr = calculate_psnr(image1, image2)
    assert psnr == 100.0

    # Test case 2: Slightly different images
    image1 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    image2 = np.array([[129, 129, 129], [129, 129, 129]], dtype=np.uint8)
    psnr = calculate_psnr(image1, image2)
    assert np.isclose(psnr, 99.845, atol=0.01)

    # Test case 3: Large difference
    image1 = np.array([[0, 0, 0], [0, 0, 0]], dtype=np.uint8)
    image2 = np.array([[255, 255, 255], [255, 255, 255]], dtype=np.uint8)
    psnr = calculate_psnr(image1, image2)
    assert np.isclose(psnr, 15.96, atol=0.01)

    # Test case 4: Edge case with zero mse
    image1 = np.array([[1, 1, 1], [1, 1, 1]], dtype=np.uint8)
    image2 = np.array([[1, 1, 1], [1, 1, 1]], dtype=np.uint8)
    psnr = calculate_psnr(image1, image2)
    assert psnr == float('inf')

    # Test case 5: Wikipedia example
    image1 = np.array([[100, 100, 100], [100, 100, 100]], dtype=np.uint8)
    image2 = np.array([[100, 100, 100], [100, 99, 99]], dtype=np.uint8)
    psnr = calculate_psnr(image1, image2)
    assert np.isclose(psnr, 31.53, atol=0.01)