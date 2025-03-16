from typing import List

def generate_gray_code(bit_count: int) -> List[int]:
    return [i ^ (i >> 1) for i in range(2 ** bit_count)]