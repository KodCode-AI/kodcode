from solution import *

import pytest
from solution import is_valid_identifier

def test_is_valid_identifier():
    assert is_valid_identifier("myIdentifier123") == True
    assert is_valid_identifier("123myIdentifier") == False
    assert is_valid_identifier("for") == False
    assert is_valid_identifier("") == False
    assert is_valid_identifier("validIdentifier") == True
    assert is_valid_identifier("Invalid-Identifier") == False  # Contains invalid character '-'
    assert is_valid_identifier("valid2023") == True
    assert is_valid_identifier("2023Invalid") == False  # Starts with a number
    assert is_valid_identifier("ValidIdentifier123") == True

def test_is_valid_identifier_empty_string():
    assert is_valid_identifier("") == False

def test_is_valid_identifier_non_string_input():
    assert is_valid_identifier(123) == False

def test_is_valid_identifier_keyword():
    assert is_valid_identifier("class") == False

def test_is_valid_identifier_capitalized():
    assert is_valid_identifier("MyIdentifier") == False


This set of tests covers a variety of scenarios, ensuring that the function behaves as expected for valid and invalid identifiers, including checking for keywords and special characters that are not allowed in identifiers.