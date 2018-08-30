'''
Please write a program to output a random number, which is divisible by 5 or 7, 
between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.
'''
import random
new_lst = [ i for i in range(101) if i % 5 == 0 and i % 7 == 0]
random_new_lst = random.choice(new_lst)
print(random_new_lst)

