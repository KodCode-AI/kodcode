def search_value_in_matrix(matrix, value):
    """
    Performs a 2D matrix binary search to find the given value.
    """
    if not matrix or not matrix[0]:
        return [-1, -1]
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == value:
            return [mid // cols, mid % cols]
        elif mid_value < value:
            left = mid + 1
        else:
            right = mid - 1
    
    return [-1, -1]