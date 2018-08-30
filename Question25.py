'''
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later

'''

class Person:
    age = 15
    def __init__(self, name, age1=age):
        self.name = name
        self.age = age1


person1 = Person('Diogo', 17)
person2 = Person('Diana')

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)
    