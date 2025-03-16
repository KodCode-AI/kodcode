def binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    elif k == 0 or k == n:
        return 1
    else:
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)