from typing import List

def fibonacci(n: int) -> List[int]:
    a, b = 0, 1
    fibs = []
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs