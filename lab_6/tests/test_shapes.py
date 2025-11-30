import pytest
import math
from src.geometry.shapes import Circle, Rectangle, Triangle

class TestCircle:
    def test_circle_creation_valid_radius(self):
        circle = Circle(5.0)
        assert circle.radius == 5.0
    
    def test_circle_creation_invalid_radius(self):
        with pytest.raises(ValueError, match="Radius must be positive"):
            Circle(-1)
        with pytest.raises(ValueError, match="Radius must be positive"):
            Circle(0)
    
    def test_circle_area(self):
        circle = Circle(2.0)
        expected_area = math.pi * 4.0
        assert math.isclose(circle.area(), expected_area)
    
    def test_circle_perimeter(self):
        circle = Circle(3.0)
        expected_perimeter = 2 * math.pi * 3.0
        assert math.isclose(circle.perimeter(), expected_perimeter)
    
    def test_circle_equality(self):
        circle1 = Circle(5.0)
        circle2 = Circle(5.0)
        circle3 = Circle(3.0)
        
        assert circle1 == circle2
        assert circle1 != circle3
        assert circle1 != "not a circle"

class TestRectangle:
    def test_rectangle_creation_valid_dimensions(self):
        rect = Rectangle(4.0, 5.0)
        assert rect.width == 4.0
        assert rect.height == 5.0
    
    def test_rectangle_creation_invalid_dimensions(self):
        with pytest.raises(ValueError):
            Rectangle(-1, 5)
        with pytest.raises(ValueError):
            Rectangle(4, 0)
    
    def test_rectangle_area(self):
        rect = Rectangle(3.0, 4.0)
        assert rect.area() == 12.0
    
    def test_rectangle_perimeter(self):
        rect = Rectangle(3.0, 4.0)
        assert rect.perimeter() == 14.0
    
    def test_rectangle_is_square(self):
        square = Rectangle(5.0, 5.0)
        non_square = Rectangle(4.0, 5.0)
        
        assert square.is_square() is True
        assert non_square.is_square() is False

class TestTriangle:
    def test_triangle_creation_valid_sides(self):
        triangle = Triangle(3.0, 4.0, 5.0)
        assert triangle.side_a == 3.0
        assert triangle.side_b == 4.0
        assert triangle.side_c == 5.0
    
    def test_triangle_creation_invalid_sides(self):
        with pytest.raises(ValueError):
            Triangle(0, 4, 5)
        with pytest.raises(ValueError):
            Triangle(1, 2, 10)  # Violates triangle inequality
    
    def test_triangle_area(self):
        triangle = Triangle(3.0, 4.0, 5.0)
        expected_area = 6.0
        assert math.isclose(triangle.area(), expected_area)
    
    def test_triangle_perimeter(self):
        triangle = Triangle(3.0, 4.0, 5.0)
        assert triangle.perimeter() == 12.0
    
    def test_triangle_type_detection(self):
        equilateral = Triangle(3.0, 3.0, 3.0)
        isosceles = Triangle(3.0, 3.0, 4.0)
        scalene = Triangle(3.0, 4.0, 5.0)
        
        assert equilateral.is_equilateral() is True
        assert isosceles.is_isosceles() is True
        assert scalene.is_isosceles() is False
