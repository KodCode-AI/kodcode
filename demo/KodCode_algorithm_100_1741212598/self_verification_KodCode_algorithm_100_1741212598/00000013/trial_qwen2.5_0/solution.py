def manhattan_distance_improved(point_a, point_b):
    """
    Calculate the Manhattan distance between two points in an n-dimensional space.

    Parameters:
    point_a (list): The first point in the n-dimensional space.
    point_b (list): The second point in the n-dimensional space.

    Returns:
    float: The Manhattan distance between point_a and point_b.

    Raises:
    ValueError: If the points do not have the same number of dimensions.
    TypeError: If the inputs are not lists of numbers.
    """
    # Check if inputs are lists
    if not isinstance(point_a, list) or not isinstance(point_b, list):
        raise TypeError("Expected a list of numbers as input, found {}".format(type(point_a).__name__))

    # Check if all elements in the lists are numbers
    if not all(isinstance(coord, (int, float)) for coord in point_a) or not all(isinstance(coord, (int, float)) for coord in point_b):
        raise TypeError("Expected a list of numbers as input")

    # Check if points have the same number of dimensions
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")

    # Calculate the Manhattan distance
    return sum(abs(a - b) for a, b in zip(point_a, point_b))