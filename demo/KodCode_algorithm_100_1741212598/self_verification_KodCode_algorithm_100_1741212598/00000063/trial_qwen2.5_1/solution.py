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
    if not (0 <= angle <= 360):
        raise ValueError("Angle must be between 0 and 360 degrees.")
    if not (1 <= scale <= 1000) or not (1 <= distance <= 1000):
        raise ValueError("Scale and distance must be between 1 and 1000.")

    angle_rad = math.radians(angle)
    rotation_matrix = None

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
    else:
        raise ValueError("Axis must be 'x', 'y', or 'z'.")

    rotated_point = [
        x * rotation_matrix[0][0] + y * rotation_matrix[1][0] + z * rotation_matrix[2][0],
        x * rotation_matrix[0][1] + y * rotation_matrix[1][1] + z * rotation_matrix[2][1],
        x * rotation_matrix[0][2] + y * rotation_matrix[1][2] + z * rotation_matrix[2][2]
    ]

    projected_x = (rotated_point[0] * scale) / (distance + rotated_point[2])
    projected_y = (rotated_point[1] * scale) / (distance + rotated_point[2])

    return projected_x, projected_y