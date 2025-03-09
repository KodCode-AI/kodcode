from solution import *

import pytest

def test_to_disjunctive_normal_form():
    # Test cases for the to_disjunctive_normal_form function
    assert to_disjunctive_normal_form("x and y") == "(x & y)"
    assert to_disjunctive_normal_form("not x and y") == "((~x) & y)"
    assert to_disjunctive_normal_form("x or y") == "(x | y)"
    assert to_disjunctive_normal_form("not x or y") == "(((~x) | y))"
    assert to_disjunctive_normal_form("not x and not y") == "((~x) & (~y))"
    assert to_disjunctive_normal_form("not (x and y)") == "((~(x & y)))"
    assert to_disjunctive_normal_form("true and x") == "(True & x)"
    assert to_disjunctive_normal_form("false or y") == "(((False) | y))"

    # Edge cases
    assert to_disjunctive_normal_form("x") == "x"
    assert to_disjunctive_normal_form("not x") == "~x"
    assert to_disjunctive_normal_form("true") == "True"
    assert to_disjunctive_normal_form("false") == "False"

def test_to_disjunctive_normal_form_invalid_syntax():
    # Invalid formula should throw a ValueError
    with pytest.raises(ValueError):
        to_disjunctive_normal_form("x and")

def test_to_disjunctive_normal_form_malformed():
    # Malformed formula should not evaluate correctly
    assert to_disjunctive_normal_form("x and y or") == "(x & y & ~y)"
    assert to_disjunctive_normal_form("x and y or not z") == "(x & y & (~z))"