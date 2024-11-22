# Area Calculations: Rectangle, Circle, and Triangle

This project provides Python functions to calculate the area of geometric shapes: rectangles, circles, and triangles. It includes unit tests to ensure code correctness and maintainability.

---

## **Functions**

### 1. `calculate_rectangle_area(length, width)`
- **Description**: Calculates the area of a rectangle.
- **Parameters**:
  - `length` (float): The length of the rectangle. Must be non-negative.
  - `width` (float): The width of the rectangle. Must be non-negative.
- **Returns**: The area of the rectangle as a float.
- **Raises**: 
  - `ValueError` if `length` or `width` is negative.

#### Example Usage:
```python
from areas import calculate_rectangle_area

# Example 1: Basic rectangle
area = calculate_rectangle_area(5, 10)
print(area)  # Output: 50

# Example 2: Zero width
area = calculate_rectangle_area(10, 0)
print(area)  # Output: 0

# Example 3: Negative input (raises ValueError)
area = calculate_rectangle_area(-5, 10)
# Output: ValueError: Length and width must be non-negative.
