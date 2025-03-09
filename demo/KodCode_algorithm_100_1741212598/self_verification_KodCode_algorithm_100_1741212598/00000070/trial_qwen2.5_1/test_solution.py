from solution import *

import pytest

def test_enhanced_lower_positive_numbers():
    assert enhanced_lower("Hello, World!") == "hello, world!"

def test_enhanced_lower_non_ascii():
    assert enhanced_lower("¡Hola, MUNDO!") == "¡hola, mundo!"

def test_enhanced_lower_digits():
    assert enhanced_lower("Python 3.8") == "python 3.8"

def test_enhanced_lower_already_lowercase():
    assert enhanced_lower("python 3.8") == "python 3.8"

def test_enhanced_lower_special_characters():
    assert enhanced_lower("12345") == "12345"

def test_enhanced_lower_whitespace():
    assert enhanced_lower(" café") == " café"

def test_enhanced_lower_empty_string():
    assert enhanced_lower("") == ""