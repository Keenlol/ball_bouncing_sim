import math

class Vector:

    def __init__(self, x=0, y=0):
        # assign __x and __y via their properties for input validation
        self.x = x
        self.y = y

    # all methods from previous exercises already defined here, but hidden

    # insert your new method(s) here (don't forget the indentation)

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, new_y):
        if isinstance(new_y, int) or isinstance(new_y, float):
            self.__y = new_y
        else:
            raise TypeError("y must be a number")
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, new_x):
        if isinstance(new_x, int) or isinstance(new_x, float):
            self.__x = new_x
        else:
            raise TypeError("x must be a number")
    
    def __str__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)
    
    def __truediv__(self, value):
        return Vector(self.x / value, self.y / value)
    
    def __rmul__(self, value):
        return Vector(self.x * value, self.y * value)

    @property 
    def length(self):
        return math.sqrt(math.fabs(self.x**2 + self.y**2))
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def subtract(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def multiply(self, s):
        return Vector(self.x * s, self.y * s)