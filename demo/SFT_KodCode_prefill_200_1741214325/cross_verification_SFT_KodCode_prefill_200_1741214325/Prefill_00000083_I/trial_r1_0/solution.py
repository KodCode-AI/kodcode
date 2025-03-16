import math

def area_of_circle(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle.
    
    Returns:
        float: The area of the circle.
    """
    area = math.pi * (radius ** 2)
    return area

# Example usage:
print(calculate_circle_area(5))  # Output: 78.53981634...