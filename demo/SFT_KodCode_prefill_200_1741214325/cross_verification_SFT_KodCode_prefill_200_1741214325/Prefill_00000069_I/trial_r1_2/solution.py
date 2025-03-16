def count_trailing_zeros(n):
    if n == 0:
        return 1
    count = 0
    n = abs(n)
    while n % 10 == 0:
        count += 1
        n = n // 10
    return count