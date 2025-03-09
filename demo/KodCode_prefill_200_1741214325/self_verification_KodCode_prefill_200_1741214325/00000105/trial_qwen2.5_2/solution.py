def shortest_distance_from_point_to_line(A, B, C, x, y):
    """
    Calculate the shortest distance from a point (x, y) to a line represented 
    by the equation Ax + By + C = 0.
    
    Parameters:
    A (float): Coefficient A of the line equation.
    B (float): Coefficient B of the line equation.
    C (float): Coefficient C of the line equation.
    x (float): x-coordinate of the point.
    y (float): y-coordinate of the point.
    
    Returns:
    float: The shortest distance from the point to the line.
    """
    numerator = abs(A * x + B * y + C)
    denominator = (A * A + B * B) ** 0.5
    return numerator / denominator