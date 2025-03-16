import math

def is_perfect_number(num: int) -> bool:
    if num <= 1:
        return False
    sum_div = 1  # 1 is a proper divisor for numbers greater than 1
    sqrt_num = int(math.sqrt(num))
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            other_divisor = num // i
            if other_divisor == i:
                sum_div += i
            else:
                sum_div += i + other_divisor
    return sum_div == num