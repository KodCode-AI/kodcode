from functools import lru_cache

def count_paths(m, n):
    @lru_cache(maxsize=None)
    def helper(i, j):
        if i == m - 1 and j == n - 1:
            return 1
        if i > m - 1 or j > n - 1:
            return 0
        return helper(i + 1, j) + helper(i, j + 1)
    return helper(0, 0)