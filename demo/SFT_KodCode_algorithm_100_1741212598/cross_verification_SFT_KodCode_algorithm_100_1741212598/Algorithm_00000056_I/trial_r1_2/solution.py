from typing import List

def generate_gray_code(bit_count: int) -> List[int]:
    # Check if the input is an integer
    if not isinstance(bit_count, int):
        raise TypeError("bit_count must be an integer")
    # Check if the bit count is positive
    if bit_count < 1:
        raise ValueError("bit_count must be a positive integer")
    # Calculate the maximum number in the sequence
    max_num = (1 << bit_count) - 1
    # Generate the Gray code sequence using the formula
    gray_sequence = [(i ^ (i >> 1)) for i in range(max_num + 1)]
    return gray_sequence