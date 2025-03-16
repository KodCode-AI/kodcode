from typing import List

def generate_gray_code(bit_count: int) -> List[int]:
    if bit_count == 0:
        return []
    max_num = (1 << bit_count) - 1
    gray_code = [i ^ (i >> 1) for i in range(max_num + 1)]
    return gray_code