'''
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) 
and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

'''

def dictfunc():
    di = dict()
    di[1] = 1
    di[2] = 2**2
    di[3] = 3**3
    return print(di)


dictfunc()

#With for loop:

def create_dictionary_square(num):
    d = dict()
    for x in range(1,num):
        d[x] = x ** 2
    return print(d)


a = int(input("Insert a number to create square dictionary!\n"))
create_dictionary_square(a)
