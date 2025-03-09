from typing import List

def generate_gray_code(bit_count: int) -> List[int]:
    """
    Generates an n-bit Gray code sequence.
    """
    if not isinstance(bit_count, int) or bit_count <= 0:
        raise ValueError("Input must be a positive integer.")
    
    gray_code_sequence = [0]
    
    for i in range(bit_count):
        gray_code_sequence.extend((1 << i) | x for x in reversed(gray_code_sequence))
    
    return gray_code_sequence