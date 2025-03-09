from solution import *

import numpy as np
import pytest

def test_calculate_psnr():
    image1 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    image2 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    psnr = calculate_psnr(image1, image2)
    assert np.isclose(psnr, 100.0), f"PSNR value should be 100.0 dB, got {psnr} dB"

    image3 = np.array([[128, 128, 128], [128, 128, 128]], dtype=np.uint8)
    image4 = np.array([[127, 128, 129], [128, 128, 128]], dtype=np.uint8)
    psnr = calculate_psnr(image3, image4)
    assert np.isclose(psnr, 31.5317, atol=1e-4), f"PSNR value should be 31.5317 dB, got {psnr} dB"

def test_mse_zero():
    image1 = np.array([[0, 0, 0], [0, 0, 0]], dtype=np.uint8)
    image2 = np.array([[0, 0, 0], [0, 0, 0]], dtype=np.uint8)
    psnr = calculate_psnr(image1, image2)
    assert np.isinf(psnr), "PSNR should be infinity for zero MSE"

def test_mean_squared_error():
    image1 = np.array([[1, 1, 1], [1, 1, 1]], dtype=np.uint8)
    image2 = np.array([[1, 2, 1], [1, 1, 1]], dtype=np.uint8)
    mse = np.mean((image1 - image2) ** 2)
    assert np.isclose(mse, 1/3), f"MSE value should be 1/3, got {mse}"


# Run the tests
if __name__ == "__main__":
    test_calculate_psnr()
    test_mse_zero()
    test_mean_squared_error()
    print("All tests passed.")