'''
Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.

'''

class Person:
    def getGender(self):
        return 0

class Male(Person):
    def getGender(self):
        return "My Gender is Male!"

class Female(Person):
    def getGender(self):
        return "My Gender is Female!"


person1 = Male()
print(person1.getGender())

person2 = Female()
print(person2.getGender())