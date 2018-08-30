'''
Please write a program which prints all permutations of [1,2,3]


Hints:
Use itertools.permutations() to get permutations of list.

'''

from itertools import permutations

perm = permutations([1,2,3], 3)
print(perm)
for i in perm:
    print(i)


#or

perm1 = list(permutations([1,2,3]))
print(perm1)