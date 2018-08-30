'''
Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.

'''

class Portuguese:
    def __init__(self, des):
        self.des = des

    @staticmethod
    def printNationality():
        print("Portugal")

class Portuense(Portuguese):
    pass

citizen = Portuguese('Diogo')
citizen.printNationality()
citizen2 = Portuense('Diana')
citizen2.printNationality()





