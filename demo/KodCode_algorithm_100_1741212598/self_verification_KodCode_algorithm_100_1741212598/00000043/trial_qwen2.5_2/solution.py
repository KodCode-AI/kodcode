from decimal import Decimal, getcontext

def calculate_pi_efficient(precision):
    """
    Calculates π to the given precision using the Bailey-Borwein-Plouffe (BBP) formula.
    """
    def bbp_formula(k):
        return (1 / (16**k)) * (4 / (8*k + 1) - (2 / (8*k + 4)) - (1 / (8*k + 5)) - (1 / (8*k + 6)))
    
    getcontext().prec = precision + 2  # Set precision to be slightly higher to account for rounding
    pi = Decimal(0)
    for k in range(precision):
        pi += bbp_formula(k)
    pi = str(pi)[:precision+2]  # Return the required number of decimal places
    return pi.rstrip('0').rstrip('.')  # Remove trailing zeros and decimal point if necessary

def main():
    print(calculate_pi_efficient(50))

if __name__ == "__main__":
    main()