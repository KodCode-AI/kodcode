from typing import List

def sumOfMaxElements(matrix: List[List[int]]) -> int:
    """
    Returns the sum of the maximum elements in each row of the given matrix.
    """
    return sum(max(row) for row in matrix)