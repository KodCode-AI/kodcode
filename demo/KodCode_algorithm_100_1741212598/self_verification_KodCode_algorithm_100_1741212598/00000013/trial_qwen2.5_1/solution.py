def manhattan_distance_improved(point_a, point_b):
    """
    Returns the Manhattan distance between two points in an n-dimensional space.
    Raises ValueError if points do not have the same number of dimensions.
    Raises TypeError if the inputs are not lists of numbers.
    """
    if not isinstance(point_a, list) or not isinstance(point_b, list):
        raise TypeError("Expected a list of numbers as input, found {}".format(type(point_a).__name__))
    if not all(isinstance(x, (int, float)) for x in point_a + point_b):
        raise TypeError("Expected a list of numbers as input, found invalid elements")
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")
    
    return sum(abs(a - b) for a, b in zip(point_a, point_b))