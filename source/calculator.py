import math
from .shapes import Shape

class GeometryCalculator:
    @staticmethod
    def total_area(shapes):
        if not shapes:
            return 0
        if not all(isinstance(shape, Shape) for shape in shapes):
            raise TypeError("All objects must be instances of Shape")
        return sum(shape.area() for shape in shapes)
    
    @staticmethod
    def total_perimeter(shapes):
        if not shapes:
            return 0
        if not all(isinstance(shape, Shape) for shape in shapes):
            raise TypeError("All objects must be instances of Shape")
        return sum(shape.perimeter() for shape in shapes)
    
    @staticmethod
    def scale_shape(shape, factor):
        if factor <= 0:
            raise ValueError("Scale factor must be positive")
        
        from .shapes import Circle, Rectangle, Triangle
        
        if isinstance(shape, Circle):
            return Circle(shape.radius * factor)
        elif isinstance(shape, Rectangle):
            return Rectangle(shape.width * factor, shape.height * factor)
        elif isinstance(shape, Triangle):
            return Triangle(shape.side_a * factor, shape.side_b * factor, shape.side_c * factor)
        else:
            raise TypeError("Unsupported shape type")
    
    @staticmethod
    def find_largest_shape_by_area(shapes):
        if not shapes:
            return None
        return max(shapes, key=lambda shape: shape.area())
