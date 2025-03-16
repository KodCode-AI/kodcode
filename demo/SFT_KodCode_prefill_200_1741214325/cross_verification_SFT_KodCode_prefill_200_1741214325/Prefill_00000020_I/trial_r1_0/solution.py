def triangle_area(base, height):
    """
    Calculate and return the area of a triangle given its base and height.
    
    Args:
        base (float): The base length of the triangle.
        height (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    """
    # First, check if the inputs are valid (positive numbers)
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    
    # Calculate the area using the formula (base * height) / 2
    area = (base * height) / 2
    
    # Return the computed area
    return area

# Example usage:
base = 5
height = 10
print(f"The area of the triangle with base {base} and height {height} is {calculate_triangle_area(base, height)}")