def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    :param length: Length of the rectangle (must be non-negative)
    :param width: Width of the rectangle (must be non-negative)
    :return: Area of the rectangle
    :raises ValueError: If length or width is negative
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width

import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    :param radius: Radius of the circle (must be non-negative)
    :return: Area of the circle
    :raises ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return math.pi * radius ** 2
