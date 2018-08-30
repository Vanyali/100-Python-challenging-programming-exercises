'''
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.

'''

class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        super().__init__()
        self.l = l

    def area(self):
        return self.l * self.l


shape1 = Shape()
print(shape1.area())

square1 = Square(10)
print(square1.area())

square2 = Square(5)
print(square2.area())
