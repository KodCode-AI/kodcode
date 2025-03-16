def count_paths(M, N):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def helper(i, j):
        if i == M - 1 and j == N - 1:
            return 1
        count = 0
        if i + 1 < M:
            count += helper(i + 1, j)
        if j + 1 < N:
            count += helper(i, j + 1)
        return count

    return helper(0, 0)