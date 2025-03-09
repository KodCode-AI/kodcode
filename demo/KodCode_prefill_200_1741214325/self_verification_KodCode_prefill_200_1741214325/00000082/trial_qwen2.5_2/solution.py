from sympy import symbols, And, Or, Not, to_dnf

# Define the symbols
x, y = symbols('x y')

def to_disjunctive_normal_form(formula):
    """
    Returns the disjunctive normal form (DNF) of a 2-variable boolean formula.
    
    Parameters:
    formula (str): A string representing a 2-variable boolean formula using 'x', 'y', and logical operators 'and', 'or', 'not'.

    Returns:
    str: The disjunctive normal form of the given formula.
    """
    # Use sympy's to_dnf function to convert the formula to DNF
    dnf_formula = to_dnf(formula)
    return str(dnf_formula)