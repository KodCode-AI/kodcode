from solution import *

import numpy as np

def test_enhanced_sepia():
    # Test case 1: White and black pixels, with sepia effect and brightness increase
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 50, 10)
    expected = np.array([[[191, 170, 145], [23, 12, 0]], [[91, 76, 61], [44, 41, 34]]], dtype=np.uint8)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_edge_cases():
    # Test case 2: Full brightness increase, with sepia effect
    image = np.full((2, 2, 3), 128, dtype=np.uint8)
    result = enhanced_sepia(image, 50, 100)
    expected = np.full((2, 2, 3), 255, dtype=np.uint8)
    assert np.array_equal(result, expected)

    # Test case 3: Full brightness decrease, with sepia effect
    image = np.full((2, 2, 3), 128, dtype=np.uint8)
    result = enhanced_sepia(image, 50, -100)
    expected = np.zeros((2, 2, 3), dtype=np.uint8)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_zero_factor():
    # Test case 4: No sepia effect, with brightness increase and decrease
    image = np.full((2, 2, 3), 128, dtype=np.uint8)
    result = enhanced_sepia(image, 0, 100)
    expected = np.full((2, 2, 3), 255, dtype=np.uint8)
    assert np.array_equal(result, expected)
    
    result = enhanced_sepia(image, 0, -100)
    expected = np.zeros((2, 2, 3), dtype=np.uint8)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_large_image():
    # Test case 5: Large image, with sepia effect and brightness increase
    image = np.full((100, 100, 3), 128, dtype=np.uint8)
    result = enhanced_sepia(image, 50, 10)
    expected = np.full((100, 100, 3), 191, dtype=np.uint8)
    assert np.array_equal(result, expected)