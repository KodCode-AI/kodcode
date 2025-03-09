To find the disjunctive normal form (DNF) of a 2-variable boolean formula using the sympy library in Python, we need to:

1. Define the boolean symbols (variables) for the 2 variables.
2. Parse the boolean formula using these variables.
3. Use sympy's `to_dnf` method to convert the boolean formula into its DNF form.

from sympy import symbols, And, Or, Not

def dnf_formula(A, B, formula_str):
    """
    Convert a 2-variable boolean formula to its DNF using sympy.

    :param A: First boolean variable (symbol)
    :param B: Second boolean variable (symbol)
    :param formula_str: Boolean formula string in terms of A and B, using standard logical operators (and, or, not)
    :return: DNF of the given boolean formula as a sympy expression
    """
    formula = formula_str.replace('and', '&').replace('or', '|').replace('not', '~')
    expr = eval(formula, {str(A): A, str(B): B})  # Convert string to sympy expression
    dnf_expr = expr.to_dnf(simplify=True)
    return dnf_expr