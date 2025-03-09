import math

def distance_point_to_line(point, line_point1, line_point2):
    """
    Calculates the shortest distance from a point to a line in 2D.
    :param point: A tuple (x, y) representing the point.
    :param line_point1: A tuple (x, y) representing the first point on the line.
    :param line_point2: A tuple (x, y) representing the second point on the line.
    :return: The shortest distance from the point to the line.
    """
    x1, y1 = point
    x2, y2 = line_point1
    x3, y3 = line_point2
    numerator = abs((y3 - y2) * x1 - (x3 - x2) * y1 + x3 * y2 - y3 * x2)
    denominator = math.sqrt((y3 - y2)**2 + (x3 - x2)**2)
    return numerator / denominator