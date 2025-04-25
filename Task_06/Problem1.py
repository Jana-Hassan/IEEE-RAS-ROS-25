import math
class Circle:
    def __init__(self, r):
        self.r = r
    
    def Circle_Area(self):
        return math.pi*(self.r**2)
    
    def Circle_Perimeter(self):
        return math.pi*self.r*2

r = float(input("Input the radius of the circle: "))

C = Circle(r)

print(f"Area of the circle: {C.Circle_Area()}")
print(f"Perimeter of the circle: {C.Circle_Perimeter()}")