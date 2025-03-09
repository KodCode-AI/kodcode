from typing import List

def generate_gray_code(bit_count: int) -> List[int]:
    """
    Returns the n-bit Gray code sequence as a list of integers.
    """
    if not isinstance(bit_count, int) or bit_count <= 0:
        raise ValueError("Input must be a positive integer.")
    
    gray_code = [0 for _ in range(1 << bit_count)]
    
    for i in range(1, bit_count + 1):
        count = 1 << (i - 1)
        for j in range(count, 1 << i):
            gray_code[j] = gray_code[j - count] | 1 << (i - 1)
    
    return gray_code