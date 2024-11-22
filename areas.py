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

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.

    :param base: The base of the triangle (must be non-negative).
    :param height: The height of the triangle (must be non-negative).
    :return: Area of the triangle.
    :raises ValueError: If base or height is negative.
    """
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative.")
    return 0.5 * base * height

