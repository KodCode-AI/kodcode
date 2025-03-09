from solution import *

import numpy as np

def test_enhanced_sepia():
    # Test with white background and black background
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 50, 10)
    expected_result = np.array([[[191, 170, 145], [23, 12, 0]], [[91, 76, 61], [44, 41, 34]]], dtype=np.uint8)
    assert np.array_equal(result, expected_result)

    # Test with pure sepia effect and some brightness adjustment
    image = np.array([[[255, 255, 255], [255, 0, 0]], [[0, 255, 0], [0, 0, 255]]], dtype=np.uint8)
    result = enhanced_sepia(image, 100, -50)
    expected_result = np.array([[[138, 119, 81], [234, 17, 30]], [[21, 94, 22], [23, 30, 18]]], dtype=np.uint8)
    assert np.array_equal(result, expected_result)

    # Test with edge case brightness adjustment
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 50, -100)
    expected_result = np.array([[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]], dtype=np.uint8)
    assert np.array_equal(result, expected_result)

    # Test with edge case factor adjustment
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 0, 100)
    expected_result = np.array([[[255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 255, 255]]], dtype=np.uint8)
    assert np.array_equal(result, expected_result)

    print("All tests passed!")

# Run the tests
test_enhanced_sepia()