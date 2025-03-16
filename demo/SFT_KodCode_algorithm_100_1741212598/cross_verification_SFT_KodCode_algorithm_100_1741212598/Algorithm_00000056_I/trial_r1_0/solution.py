from typing import List

def generate_gray_code(bit_count: int) -> List[int]:
    if not isinstance(bit_count, int):
        raise TypeError("bit_count must be an integer.")
    if bit_count < 1 or bit_count > 32:
        raise ValueError("bit_count must be between 1 and 32, inclusive.")
    
    n = bit_count
    max_num = (1 << n) - 1
    gray_code = []
    for i in range(max_num + 1):
        gray = i ^ (i >> 1)
        gray_code.append(gray)
    return gray_code