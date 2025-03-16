from functools import lru_cache

def number_of_paths(M, N):
    @lru_cache(maxsize=None)
    def helper(m, n):
        if m == 0 and n == 0:
            return 1
        if m == 0:
            return helper(m, n - 1)
        if n == 0:
            return helper(m - 1, n)
        return helper(m - 1, n) + helper(m, n - 1)
    
    return helper(M - 1, N - 1)