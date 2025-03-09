from solution import *

import pytest

def test_enhanced_lower_ascii():
    assert enhanced_lower("Hello, World!") == "hello, world!"
    assert enhanced_lower("¡Hola, MUNDO!") == "¡hola, mundo!"
    assert enhanced_lower("Python 3.8") == "python 3.8"
    assert enhanced_lower("12345") == "12345"
    assert enhanced_lower(" café") == " café"

def test_enhanced_lower_non_ascii():
    assert enhanced_lower("Straße") == "straße"
    assert enhanced_lower(" pozar") == " pozar"
    assert enhanced_lower("ᵟ") == "ᵟ"
    assert enhanced_lower("lingerie") == "lingerie"
    assert enhanced_lower("Ωmega") == "ωmega"

def test_enhanced_lower_empty_string():
    assert enhanced_lower("") == ""
    assert enhanced_lower(" ")[0] == " "

def test_enhanced_lower_large_string():
    large_string = "A" * 100000
    assert len(enhanced_lower(large_string)) == 100000

def test_enhanced_lower_mixed_case():
    assert enhanced_lower("UPPERlower") == "upperlower"
    assert enhanced_lower("UPPERLOWER") == "upperlower"
    assert enhanced_lower("upperLOWER") == "upperlower"