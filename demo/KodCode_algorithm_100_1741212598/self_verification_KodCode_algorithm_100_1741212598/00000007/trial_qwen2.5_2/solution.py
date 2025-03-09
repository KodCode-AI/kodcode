def search_value_in_matrix(matrix, value):
    """
    Perform a 2D matrix binary search to find the given value.
    Returns the coordinates [row, col] of the value if found, otherwise [-1, -1].
    """
    if not matrix or not matrix[0]:
        return [-1, -1]
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = matrix[mid // cols][mid % cols]
        
        if mid_val == value:
            return [mid // cols, mid % cols]
        elif mid_val < value:
            left = mid + 1
        else:
            right = mid - 1
    
    return [-1, -1]