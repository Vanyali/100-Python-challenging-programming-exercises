'''
Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

'''
from math import pi

class Circle:
    def __init__(self, r):
        self.r = r

    def circle_area(self):
        area = pi*(self.r**2)
        return area

circle_1 = Circle(5)
circle_2 = Circle(10)

print(circle_1.circle_area())
print(circle_2.circle_area())

