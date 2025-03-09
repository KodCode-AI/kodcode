from solution import *

import keyword
from solution import is_valid_identifier

def test_is_valid_identifier():
    assert is_valid_identifier('valid_identifier') == True
    assert is_valid_identifier('with_number4') == True
    assert is_valid_identifier('_underscore_start') == True
    assert is_valid_identifier('4invalid') == False
    assert is_valid_identifier('for') == False  # Python keyword
    assert is_valid_identifier('import') == False  # Python keyword
    assert is_valid_identifier('if') == False  # Python keyword
    assert is_valid_identifier('') == False
    assert is_valid_identifier('invalid-character!') == False
    assert is_valid_identifier('valid123') == True
    assert is_valid_identifier('valid_123') == True