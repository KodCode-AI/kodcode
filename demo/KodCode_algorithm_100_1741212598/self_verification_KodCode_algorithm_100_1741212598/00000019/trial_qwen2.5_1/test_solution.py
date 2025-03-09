from solution import *

import pytest

def test_enhanced_djb2():
    assert enhanced_djb2('Algorithms') == 3782405311
    assert enhanced_djb2('scramble bits', 33) == 1609059040
    assert enhanced_djb2('非ASCII', 5381) == 756778245

def test_enhanced_djb2_unicode():
    assert enhanced_djb2('😊🚀', 5381) == 2138187681
    assert enhanced_djb2('müller', 33) == 3388216817

def test_enhanced_djb2_edge_cases():
    assert enhanced_djb2(' ', 5381) == 1767789659
    assert enhanced_djb2('', 33) == 5381
    assert enhanced_djb2('a', 100) == 6611

def test_enhanced_djb2_large_string():
    large_string = 'a' * 1000  # 1000 'a' characters
    hash_value = enhanced_djb2(large_string, 5381)
    assert hash_value == 915069401

def test_enhanced_djb2_non_ascii_single_char():
    assert enhanced_djb2('müller', 33) == 3388216817
    assert enhanced_djb2('😊', 5381) == 2138187681