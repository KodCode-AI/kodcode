from typing import List
from functools import lru_cache
import math

def max_product(speed: List[int], efficiency: List[int], k: int) -> int:
    """
    Returns the maximum product of the team's average speed and the minimum efficiency.
    """
    engineers = sorted(zip(efficiency, speed), reverse=True)
    mod = 10**9 + 7
    n = len(speed)
    
    def avg_speed(arr: List[int]) -> float:
        return sum(arr) / len(arr)
    
    @lru_cache(None)
    def dp(i: int, min_eff: int, k: int) -> int:
        if k == 0 or i == n:
            if k == 0:
                return 0
            else:
                return min_eff * avg_speed(speed[:i])
        take = 0 if min_eff > engineers[i][0] else dp(i + 1, min(min_eff, engineers[i][0]), k - 1) + engineers[i][1]
        not_take = dp(i + 1, min_eff, k)
        return max(take, not_take)
    
    return dp(0, math.inf, k) % mod