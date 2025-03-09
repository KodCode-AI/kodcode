from mpmath import mp

def calculate_pi_efficient(precision):
    """
    Approximates π to the specified precision using the mpmath library for arbitrary precision calculations.
    """
    mp.dps = precision  # set the decimal precision
    return str(mp.pi)