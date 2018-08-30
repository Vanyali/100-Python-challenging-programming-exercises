'''
Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.

'''

def lst_square():
    lst = list()
    for i in range(1,21):
        lst.append(i**2)
    return tuple(lst)

print(lst_square())