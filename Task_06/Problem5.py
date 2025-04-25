import math

class Shape:
    def Area(self):
        pass
    
    def Perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def Area(self):
        return math.pi * (self.r ** 2)
    
    def Perimeter(self):
        return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def Area(self):
        return self.l * self.w
    
    def Perimeter(self):
        return 2 * (self.l + self.w)

class Triangle(Shape):
    def __init__(self, b, h, s1, s2, s3):
        self.b = b
        self.h = h
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    
    def Area(self):
        return 0.5 * self.b * self.h
    
    def Perimeter(self):
        return self.s1 + self.s2 + self.s3


circle = Circle(7)
rectangle = Rectangle(5, 7)
triangle = Triangle(5, 4, 4, 3, 5)

print(f"Radius of the circle: {circle.r}")
print(f"Circle Area: {circle.Area()}")
print(f"Circle Perimeter: {circle.Perimeter()}\n")

print(f"Rectangle: Length = {rectangle.l} Width = {rectangle.w}")
print(f"Rectangle Area: {rectangle.Area()}")
print(f"Rectangle Perimeter: {rectangle.Perimeter()}\n")

print(f"Triangle: Base = {triangle.b} Height = {triangle.h} side1 = {triangle.s1} side2 = {triangle.s2} side3 = {triangle.s3}")
print(f"Triangle Area: {triangle.Area()}")
print(f"Triangle Perimeter: {triangle.Perimeter()}")