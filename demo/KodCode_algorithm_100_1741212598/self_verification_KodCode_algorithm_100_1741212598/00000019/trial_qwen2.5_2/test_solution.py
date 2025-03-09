from solution import *

python
def test_enhanced_djb2():
    assert enhanced_djb2('Algorithms') == 3782405311
    assert enhanced_djb2('scramble bits', 33) == 1609059040
    assert enhanced_djb2('非ASCII', 5381) == 756778245

def test_enhanced_djb2_non_ascii():
    assert enhanced_djb2('你好') == 1415019453
    assert enhanced_djb2('こんにちは', 33) == 1212807467
    assert enhanced_djb2('مرحبا', 5381) == 2108705526

def test_enhanced_djb2_empty_string():
    assert enhanced_djb2('') == 5381
    assert enhanced_djb2('', 33) == 33

def test_enhanced_djb2_montonic():
    s = 'Algorithms'
    initial_constant = 5381
    new_constant = 33
    hash_with_initial = enhanced_djb2(s, initial_constant)
    hash_with_new = enhanced_djb2(s, new_constant)
    assert hash_with_initial != hash_with_new  # Ensure different constants produce different results

def test_enhanced_djb2_with_large_string():
    long_string = 'a' * 1000  # A long string to test performance
    hash_value = enhanced_djb2(long_string)
    assert isinstance(hash_value, int)  # Ensure the result is an integer