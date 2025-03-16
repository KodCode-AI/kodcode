def sum_multiples():
    def sum_multiples_of(divisor, limit):
        max_term = (limit - 1) // divisor
        return divisor * max_term * (max_term + 1) // 2
    sum3 = sum_multiples_of(3, 1000)
    sum5 = sum_multiples_of(5, 1000)
    sum15 = sum_multiples_of(15, 1000)
    return sum3 + sum5 - sum15