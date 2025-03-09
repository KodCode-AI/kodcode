from sympy import symbols, And, Or, Not, simplify

def to_dnf(boolean_formula):
    """
    Converts a 2-variable boolean formula to Disjunctive Normal Form (DNF).

    Parameters:
    boolean_formula (str): A string representing a 2-variable boolean formula, e.g., "A and not B or B"

    Returns:
    dnf (str): The DNF equivalent of the provided boolean formula
    """
    # Define symbols
    A, B = symbols('A B')
    
    # Parse the boolean formula using sympy
    parsed_formula = eval(boolean_formula)
    
    # Simplify the formula
    simplified_formula = simplify(parsed_formula)
    
    # Convert to DNF
    dnf = simplify(simplified_formula, basic=True, force=True, deep=True)
    
    return str(dnf)