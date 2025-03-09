from solution import *

import numpy as np
import pytest

def test_enhanced_sepia_positive_brightness():
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 50, 10)
    expected = np.array([[[191, 170, 145], [23, 12, 0]], [[91, 76, 61], [44, 41, 34]]], dtype=np.uint8)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_negative_brightness():
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 50, -10)
    expected = np.array([[[165, 146, 126], [16, 7, 7]], [[97, 95, 92], [54, 53, 52]]], dtype=np.uint8)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_zero_brightness():
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 50, 0)
    expected = np.array([[[168, 149, 124], [20, 11,  0]], [[98, 89, 75], [47, 44, 39]]], dtype=np.uint8)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_full_brightness():
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 50, 100)
    expected = np.array([[[249, 235, 205], [31, 19,  9]], [[186, 176, 159], [72, 68, 61]]], dtype=np.uint8)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_low_brightness():
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 50, -100)
    expected = np.array([[[15,  6,  4], [ 0,  0,  0]], [[  0,  0,  0], [ 1,  1,  2]]], dtype=np.uint8)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_zero_factor():
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 0, 0)
    expected = image
    assert np.array_equal(result, expected)

def test_enhanced_sepia_invalid_factor():
    image = np.array([[[255, 255, 255], [0, 0, 0]], [[128, 128, 128], [64, 64, 64]]], dtype=np.uint8)
    result = enhanced_sepia(image, 150, 0)
    expected = enhanced_sepia(image, 100, 0)
    assert np.array_equal(result, expected)

def test_enhanced_sepia_empty_image():
    image = np.array([], dtype=np.uint8).reshape(0, 0, 3)
    result = enhanced_sepia(image, 50, 0)
    expected = image
    assert np.array_equal(result, expected)