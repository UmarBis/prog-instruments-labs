import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return math.isclose(self.radius, other.radius)

class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return (math.isclose(self.width, other.width) and 
                math.isclose(self.height, other.height))

class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        sides = [side_a, side_b, side_c]
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive")
        if max(sides) >= sum(sides) - max(sides):
            raise ValueError("Triangle inequality violated")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self):
        # Using Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    def is_equilateral(self):
        return (math.isclose(self.side_a, self.side_b) and 
                math.isclose(self.side_b, self.side_c))
    
    def is_isosceles(self):
        return (math.isclose(self.side_a, self.side_b) or 
                math.isclose(self.side_b, self.side_c) or 
                math.isclose(self.side_a, self.side_c))
