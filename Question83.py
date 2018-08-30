'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this 
list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

'''

lst = [12,24,35,24,88,120,155,88,120,155]
lst_no_duplicate = set(lst)
print(lst_no_duplicate)


new_lst_ndupli_rever = []

for item in reversed(lst):
    if item in lst:
        new_lst_ndupli_rever.append(item)

print(new_lst_ndupli_rever)



