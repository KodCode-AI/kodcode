import math

def area_of_circle(radius):
    """
    Calculate the area of a circle using its radius.
    
    Args:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    area = math.pi * radius ** 2
    return area

# Example usage:
radius = 5  # Replace with your desired radius
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} units is {area} square units.")