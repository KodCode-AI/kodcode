def count_paths(m: int, n: int) -> int:
    a = m + n - 2
    k = min(m - 1, n - 1)
    result = 1
    for i in range(1, k + 1):
        result = result * (a - k + i) // i
    return result