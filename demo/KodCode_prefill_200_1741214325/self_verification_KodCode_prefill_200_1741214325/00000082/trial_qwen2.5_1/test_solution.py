from solution import *

from solution import dnf_formula
from sympy import symbols

# Define the symbols
A, B = symbols('A B')

def test_dnf_formula():
    assert dnf_formula(A, B, "A and B").equals(A & B)
    assert dnf_formula(A, B, "A and not B").equals(A & ~B)
    assert dnf_formula(A, B, "not A and B").equals(~A & B)
    assert dnf_formula(A, B, "not A and not B").equals(~A & ~B)
    assert dnf_formula(A, B, "A or B").equals(A | B)
    assert dnf_formula(A, B, "A or not B").equals(A | ~B)
    assert dnf_formula(A, B, "not A or B").equals(~A | B)
    assert dnf_formula(A, B, "not A or not B").equals(~A | ~B)
    assert dnf_formula(A, B, "(A and not B) or (not A and B)").equals((A & ~B) | (~A & B))  # XOR DNF
    assert dnf_formula(A, B, "(not A and B) or (A and not B)").equals((~A & B) | (A & ~B))  # XOR DNF

if __name__ == "__main__":
    import pytest
    pytest.main()