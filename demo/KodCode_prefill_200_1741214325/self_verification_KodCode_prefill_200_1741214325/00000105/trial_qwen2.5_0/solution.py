import math

def shortest_distance_from_point_to_line(point, line):
    """
    Calculates the shortest distance from a point to a line in a 2D plane.
    
    Args:
    point: A tuple (x, y) representing the point.
    line: A tuple ((x1, y1), (x2, y2)) representing two points that define the line.
    
    Returns:
    The shortest distance from the point to the line.
    """
    x, y = point
    x1, y1 = line[0]
    x2, y2 = line[1]
    
    # Line equation parameters
    A = y2 - y1
    B = x1 - x2
    C = (y2 - y1) * x1 - (x2 - x1) * y1
    
    # Distance from point to line
    distance = abs(A * x + B * y + C) / math.sqrt(A**2 + B**2)
    return distance