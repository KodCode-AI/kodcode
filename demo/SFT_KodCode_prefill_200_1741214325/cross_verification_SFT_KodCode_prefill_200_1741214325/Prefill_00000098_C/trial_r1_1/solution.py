from typing import List

def fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fibs = [0, 1]
        while len(fibs) < n:
            next_term = fibs[-1] + fibs[-2]
            fibs.append(next_term)
        return fibs