from solution import *

import pytest

def test_enhanced_lower_ascii():
    assert enhanced_lower("Hello, World!") == 'hello, world!'
    assert enhanced_lower("¡Hola, MUNDO!") == '¡hola, mundo!'
    assert enhanced_lower("Python 3.8") == 'python 3.8'
    assert enhanced_lower("12345") == '12345'
    assert enhanced_lower(" café") == ' café'

def test_enhanced_lower_non_ascii():
    assert enhanced_lower("Καλημέρα") == 'καλημέρα'
    assert enhanced_lower("😀.prop") == '😀.prop'
    assert enhanced_lower(" teasers") == ' teasers'
    assert enhanced_lower("Teasers") == 'teasers'
    assert enhanced_lower("Teasers😀") == 'teasers😀'