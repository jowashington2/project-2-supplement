import unittest
from areas import calculate_rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)
    
    def test_zero_length(self):
        self.assertEqual(calculate_rectangle_area(0, 10), 0)
    
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-5, 10)
