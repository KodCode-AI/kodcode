def is_perfect_number(num: int) -> bool:
    if num <= 1:
        return False
    sum_div = 1
    sqrt_num = int(num ** 0.5)
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            other_divisor = num // i
            if i == other_divisor:
                sum_div += i
            else:
                sum_div += i + other_divisor
    return sum_div == num