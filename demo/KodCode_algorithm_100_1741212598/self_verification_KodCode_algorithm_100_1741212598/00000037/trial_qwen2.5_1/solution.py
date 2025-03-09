from functools import lru_cache

def optimized_partition(n: int) -> int:
    """
    Returns the smallest integer n such that p(n) is divisible by one million.
    """
    @lru_cache(maxsize=None)
    def partition_k(n: int, k: int) -> int:
        if n == 0:
            return 1
        if n < 0 or k == 0:
            return 0
        return partition_k(n - k, k) + partition_k(n - 1, k - 1)
    
    n = 1
    while True:
        count = 0
        for k in range(1, n + 1):
            count += partition_k(n, k)
        if count % 1000000 == 0:
            return n
        n += 1