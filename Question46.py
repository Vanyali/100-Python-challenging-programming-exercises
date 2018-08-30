'''
Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.

'''

class Portuguese:
    @staticmethod
    def printNationality():
        print("Portugal")


user = Portuguese()
user.printNationality()
Portuguese.printNationality()

#Review Staticmethod!