import math

def rotate_and_project(x: float, y: float, z: float, axis: str, angle: float, scale: float, distance: float) -> tuple[float, float]:
    """
    Rotate a 3D point around a specified axis and then convert it to a 2D point for rendering.
    """
    # Validate input types and ranges
    if not all(isinstance(val, (int, float)) for val in [x, y, z, angle, scale, distance]):
        raise ValueError("All input values must be integers or floats.")
    if not -1000 <= x <= 1000 or not -1000 <= y <= 1000 or not -1000 <= z <= 1000:
        raise ValueError("3D point coordinates must be between -1000 and 1000.")
    if not 0 <= angle <= 360:
        raise ValueError("Angle must be between 0 and 360 degrees.")
    if not 1 <= scale <= 1000 or not 1 <= distance <= 1000:
        raise ValueError("Scale and distance must be between 1 and 1000.")

    # Normalize angle to be in the range [0, 360]
    angle = angle % 360

    # Handle rotation around x-axis
    if axis == 'x':
        rotation_matrix = [
            [1, 0, 0],
            [0, math.cos(math.radians(angle)), -math.sin(math.radians(angle))],
            [0, math.sin(math.radians(angle)), math.cos(math.radians(angle))]
        ]
    # Handle rotation around y-axis
    elif axis == 'y':
        rotation_matrix = [
            [math.cos(math.radians(angle)), 0, math.sin(math.radians(angle))],
            [0, 1, 0],
            [-math.sin(math.radians(angle)), 0, math.cos(math.radians(angle))]
        ]
    # Handle rotation around z-axis
    elif axis == 'z':
        rotation_matrix = [
            [math.cos(math.radians(angle)), -math.sin(math.radians(angle)), 0],
            [math.sin(math.radians(angle)), math.cos(math.radians(angle)), 0],
            [0, 0, 1]
        ]
    else:
        raise ValueError("Rotation axis must be 'x', 'y', or 'z'.")

    # Apply rotation
    rotated_point = [
        rotation_matrix[0][0] * x + rotation_matrix[0][1] * y + rotation_matrix[0][2] * z,
        rotation_matrix[1][0] * x + rotation_matrix[1][1] * y + rotation_matrix[1][2] * z,
        rotation_matrix[2][0] * x + rotation_matrix[2][1] * y + rotation_matrix[2][2] * z
    ]

    # Apply perspective projection
    z_prime = distance - rotated_point[2]
    projected_x = scale * (rotated_point[0] / z_prime)
    projected_y = scale * (rotated_point[1] / z_prime)

    return (projected_x, projected_y)