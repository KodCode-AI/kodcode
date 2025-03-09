from solution import *

from solution import to_dnf

def test_to_dnf():
    assert to_dnf("A and not B") == "A & ~B"
    assert to_dnf("A or B") == "(A | B)"
    assert to_dnf("not A and B") == "~A & B"
    assert to_dnf("A and B") == "(A & B)"
    assert to_dnf("not A or not B") == "(~A | ~B)"
    assert to_dnf("(A and not B) or (not A and B)") == "((A & ~B) | (~A & B))"
    assert to_dnf("(A or B) and (not A or B)") == "((A | B) & (~A | B))"
    assert to_dnf("(A and B) or (A and not B) or (not A and B)") == "((A & B) | (A & ~B) | (~A & B))"