from decimal import Decimal, getcontext

def calculate_pi_efficient(precision):
    """
    Approximates pi to the given precision using the AGM (Arithmetic-Geometric Mean) method.
    """
    getcontext().prec = precision + 2  # Set precision to be safe and add extra for accuracy

    def agm(a, b, epsilon):
        while abs(a - b) > epsilon:
            a_next = (a + b) / 2
            b_next = (a * b)**0.5
            a, b = a_next, b_next
        return a

    a = Decimal(1)
    b = Decimal(1).sqrt()
    pi = Decimal(4) * (a + b) * (a + b) / (4 * a)
    return str(pi.quantize(Decimal('1.' + '0' * precision)))