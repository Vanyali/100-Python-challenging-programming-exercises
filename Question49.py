'''
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        total_area = self.length * self.width
        return total_area

rectangle_1 = Rectangle(5,5)
rectangle_2 = Rectangle(10,5)

print(rectangle_1.rectangle_area())
print(rectangle_2.rectangle_area())

