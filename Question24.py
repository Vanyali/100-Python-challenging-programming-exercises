'''
Question:
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books.
But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function

'''
#for example....
print(abs.__doc__)
print(int.__doc__)
print(float.__doc__)
print(isinstance.__doc__)
print(InterruptedError.__doc__)
print(str.__doc__)
print(sorted.__doc__)
print(reversed.__doc__)


#On my own

def squarefunc(n):
    '''
        Just simply function to square the number given.
    '''
    return n**2

#Gonna show up the triple string above, inside the function!
print(squarefunc.__doc__)

