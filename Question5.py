'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

class outstring:
    def __init__(self):
        self.string = ''

    def getString(self):
        self.string = input("Write a sentence!")
    
    def print_string(self):
        print(self.string)

test = outstring()
test.print_string()
test.getString()
test.print_string()