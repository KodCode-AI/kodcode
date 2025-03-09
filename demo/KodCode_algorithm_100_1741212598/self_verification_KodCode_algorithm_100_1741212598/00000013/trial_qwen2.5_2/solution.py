def manhattan_distance_improved(point_a, point_b):
    """
    Calculate the Manhattan distance between two points in n-dimensional space.
    """
    # Check if inputs are lists
    if not isinstance(point_a, list) or not isinstance(point_b, list):
        raise TypeError("Expected a list of numbers as input, found {}".format(type(point_a).__name__))
    
    # Check if points are in the same n-dimensional space
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")
    
    # Calculate Manhattan distance
    distance = sum(abs(a - b) for a, b in zip(point_a, point_b))
    
    return float(distance)