import unittest
from areas import calculate_circle_area, calculate_rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)
    
    def test_zero_length(self):
        self.assertEqual(calculate_rectangle_area(0, 10), 0)
    
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-5, 10)

class TestCircleArea(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(calculate_circle_area(5), 78.54, places=2)

    def test_zero_radius(self):
        self.assertEqual(calculate_circle_area(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_circle_area(-5)
import unittest
from areas import calculate_triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(calculate_triangle_area(10, 5), 25)
        self.assertEqual(calculate_triangle_area(7, 3), 10.5)

    def test_zero_values(self):
        self.assertEqual(calculate_triangle_area(0, 5), 0)
        self.assertEqual(calculate_triangle_area(10, 0), 0)

    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_triangle_area(-10, 5)
        with self.assertRaises(ValueError):
            calculate_triangle_area(10, -5)
        with self.assertRaises(ValueError):
            calculate_triangle_area(-10, -5)
