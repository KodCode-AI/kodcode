def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    a_abs = abs(a)
    b_abs = abs(b)
    return (a_abs * b_abs) // gcd(a_abs, b_abs)