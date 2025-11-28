import pytest
import math
from src.geometry.shapes import Circle, Rectangle, Triangle
from src.geometry.calculator import GeometryCalculator

class TestGeometryCalculator:
    def test_total_area_empty_list(self):
        assert GeometryCalculator.total_area([]) == 0
    
    def test_total_area_mixed_shapes(self):
        circle = Circle(1.0)  # area = π
        rectangle = Rectangle(2.0, 3.0)  # area = 6
        triangle = Triangle(3.0, 4.0, 5.0)  # area = 6
        
        shapes = [circle, rectangle, triangle]
        expected_total = math.pi + 6 + 6
        actual_total = GeometryCalculator.total_area(shapes)
        
        assert math.isclose(actual_total, expected_total)
    
    def test_total_area_invalid_objects(self):
        with pytest.raises(TypeError):
            GeometryCalculator.total_area([Circle(1), "not a shape"])
    
    def test_total_perimeter(self):
        circle = Circle(1.0)  # perimeter = 2π
        rectangle = Rectangle(2.0, 3.0)  # perimeter = 10
        
        shapes = [circle, rectangle]
        expected_total = 2 * math.pi + 10
        actual_total = GeometryCalculator.total_perimeter(shapes)
        
        assert math.isclose(actual_total, expected_total)

    # Параметризованный тест - более сложный тест
    @pytest.mark.parametrize("radius,expected_area,expected_perimeter", [
        (1.0, math.pi, 2 * math.pi),
        (2.0, 4 * math.pi, 4 * math.pi),
        (0.5, 0.25 * math.pi, math.pi),
    ])
    def test_circle_properties_parametrized(self, radius, expected_area, expected_perimeter):
        circle = Circle(radius)
        assert math.isclose(circle.area(), expected_area)
        assert math.isclose(circle.perimeter(), expected_perimeter)

    # Еще один параметризованный тест для прямоугольников
    @pytest.mark.parametrize("width,height,is_square", [
        (5, 5, True),
        (4, 5, False),
        (10, 10, True),
        (1, 2, False),
    ])
    def test_rectangle_square_detection_parametrized(self, width, height, is_square):
        rect = Rectangle(width, height)
        assert rect.is_square() == is_square

    # Тест с использованием моков - более сложный тест
    def test_find_largest_shape_with_mock(self, mocker):
        # Создаем моки фигур с разными площадями
        mock_shape_small = mocker.Mock()
        mock_shape_small.area.return_value = 10.0
        
        mock_shape_medium = mocker.Mock()
        mock_shape_medium.area.return_value = 20.0
        
        mock_shape_large = mocker.Mock()
        mock_shape_large.area.return_value = 30.0
        
        shapes = [mock_shape_small, mock_shape_medium, mock_shape_large]
        largest = GeometryCalculator.find_largest_shape_by_area(shapes)
        
        assert largest == mock_shape_large
        # Проверяем, что метод area() вызывался для каждой фигуры
        mock_shape_small.area.assert_called_once()
        mock_shape_medium.area.assert_called_once()
        mock_shape_large.area.assert_called_once()

    def test_scale_shape_circle(self):
        original = Circle(2.0)
        scaled = GeometryCalculator.scale_shape(original, 3.0)
        
        assert isinstance(scaled, Circle)
        assert math.isclose(scaled.radius, 6.0)
        assert math.isclose(scaled.area(), math.pi * 36.0)

    def test_scale_shape_rectangle(self):
        original = Rectangle(2.0, 3.0)
        scaled = GeometryCalculator.scale_shape(original, 2.0)
        
        assert isinstance(scaled, Rectangle)
        assert math.isclose(scaled.width, 4.0)
        assert math.isclose(scaled.height, 6.0)
        assert math.isclose(scaled.area(), 24.0)

    def test_scale_shape_invalid_factor(self):
        circle = Circle(1.0)
        with pytest.raises(ValueError, match="Scale factor must be positive"):
            GeometryCalculator.scale_shape(circle, -1.0)
        with pytest.raises(ValueError, match="Scale factor must be positive"):
            GeometryCalculator.scale_shape(circle, 0.0)

    def test_find_largest_shape_empty_list(self):
        assert GeometryCalculator.find_largest_shape_by_area([]) is None

    def test_find_largest_shape_single_element(self):
        circle = Circle(2.0)
        shapes = [circle]
        largest = GeometryCalculator.find_largest_shape_by_area(shapes)
        
        assert largest == circle
