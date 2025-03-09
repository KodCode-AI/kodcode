import math

def rotate_and_project(x: float, y: float, z: float, axis: str, angle: float, scale: float, distance: float) -> tuple[float, float]:
    """
    Rotate a 3D point around a specified axis and then convert it to a 2D point for rendering.

    :param x: x-coordinate of the 3D point.
    :param y: y-coordinate of the 3D point.
    :param z: z-coordinate of the 3D point.
    :param axis: Axis around which to rotate ('x', 'y', 'z').
    :param angle: Angle of rotation in degrees.
    :param scale: Scale factor for the 2D projection.
    :param distance: Viewing distance for the perspective projection.
    :return: A tuple (projected_x, projected_y) representing the 2D point.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
        raise ValueError("Coordinates must be int or float.")
    if not (isinstance(angle, (int, float))) or not (0 <= angle <= 360):
        raise ValueError("Angle must be a float between 0 and 360 degrees.")
    if not (isinstance(scale, (int, float))) or not (1 <= scale <= 1000):
        raise ValueError("Scale must be a float between 1 and 1000.")
    if not (isinstance(distance, (int, float))) or not (1 <= distance <= 1000):
        raise ValueError("Distance must be a float between 1 and 1000.")
    
    angle_rad = math.radians(angle)

    if axis not in ('x', 'y', 'z'):
        raise ValueError("Invalid axis. Must be one of 'x', 'y', 'z'.")

    if axis == 'x':
        rotation_matrix = [
            [1, 0, 0],
            [0, math.cos(angle_rad), -math.sin(angle_rad)],
            [0, math.sin(angle_rad), math.cos(angle_rad)]
        ]
    elif axis == 'y':
        rotation_matrix = [
            [math.cos(angle_rad), 0, math.sin(angle_rad)],
            [0, 1, 0],
            [-math.sin(angle_rad), 0, math.cos(angle_rad)]
        ]
    elif axis == 'z':
        rotation_matrix = [
            [math.cos(angle_rad), -math.sin(angle_rad), 0],
            [math.sin(angle_rad), math.cos(angle_rad), 0],
            [0, 0, 1]
        ]

    # Rotate the 3D point
    rotated_point = [
        rotation_matrix[0][0] * x + rotation_matrix[0][1] * y + rotation_matrix[0][2] * z,
        rotation_matrix[1][0] * x + rotation_matrix[1][1] * y + rotation_matrix[1][2] * z,
        rotation_matrix[2][0] * x + rotation_matrix[2][1] * y + rotation_matrix[2][2] * z
    ]

    # Project to 2D screen space using perspective projection
    projected_x = rotated_point[0] / (rotated_point[2] + distance) * scale + scale
    projected_y = rotated_point[1] / (rotated_point[2] + distance) * scale + scale

    return (projected_x, projected_y)