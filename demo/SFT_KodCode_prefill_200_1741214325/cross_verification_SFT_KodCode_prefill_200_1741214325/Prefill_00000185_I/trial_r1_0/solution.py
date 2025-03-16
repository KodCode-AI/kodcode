def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return (abs(a) * abs(b)) // gcd(abs(a), abs(b))