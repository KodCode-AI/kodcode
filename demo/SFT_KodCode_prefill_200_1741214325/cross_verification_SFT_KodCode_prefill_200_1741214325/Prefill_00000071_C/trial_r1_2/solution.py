def sum_of_multiples() -> int:
    max_num = 999
    m3 = max_num // 3
    sum3 = 3 * m3 * (m3 + 1) // 2
    m5 = max_num // 5
    sum5 = 5 * m5 * (m5 + 1) // 2
    m15 = max_num // 15
    sum15 = 15 * m15 * (m15 + 1) // 2
    return sum3 + sum5 - sum15