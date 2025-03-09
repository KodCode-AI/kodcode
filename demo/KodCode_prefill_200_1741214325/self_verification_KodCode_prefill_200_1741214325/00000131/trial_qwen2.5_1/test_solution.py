from solution import *

from solution import reverse_string

def test_reverse_string_empty():
    assert reverse_string('') == ''

def test_reverse_string_single_character():
    assert reverse_string('a') == 'a'
    assert reverse_string(9) == '9'

def test_reverse_string_lowercase():
    assert reverse_string('hello') == 'olleh'
    
def test_reverse_string_uppercase():
    assert reverse_string('WORLD') == 'DLROW'
    
def test_reverse_string_mixed_case():
    assert reverse_string('HelloWorld') == 'dlroWolleH'
    
def test_reverse_string_with_spaces():
    assert reverse_string('   ') == '   '
    
def test_reverse_string_with_integers():
    assert reverse_string(12345) == '54321'