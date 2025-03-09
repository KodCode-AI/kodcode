from solution import *

import pytest

def test_enhanced_djb2():
    assert enhanced_djb2('Algorithms') == 3782405311
    assert enhanced_djb2('scramble bits', 33) == 1609059040
    assert enhanced_djb2('非ASCII', 5381) == 756778245

def test_enhanced_djb2_non_ascii():
    assert enhanced_djb2('你好', 5381) == 632538182
    assert enhanced_djb2('こんにちは', 33) == 581382360
    assert enhanced_djb2('안녕하세요', 5381) == 623096277

def test_enhanced_djb2_empty_string():
    assert enhanced_djb2('') == 5381
    assert enhanced_djb2('', 33) == 33

def test_enhanced_djb2_single_character():
    assert enhanced_djb2('A') == 2239020883
    assert enhanced_djb2('A', 5381) == 2239020883

def test_enhanced_djb2_large_string():
    assert enhanced_djb2('a' * 1000, 5381) == 3410771441763555825
    assert enhanced_djb2('abc' * 333, 33) == 1427915927173384407