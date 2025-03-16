def sum_of_multiples() -> int:
    def sum_multiple(k):
        n = 999 // k
        return k * n * (n + 1) // 2
    
    sum3 = sum_multiple(3)
    sum5 = sum_multiple(5)
    sum15 = sum_multiple(15)
    
    return sum3 + sum5 - sum15