'''
Please generate a random float where the value is between 10 and 100 using Python math module.
Hints:
Use random.random() to generate a random float in [0,1].
'''

import random as r

inc = r.uniform(10,100)
print(inc)


#Other solution

inc1 = r.random()*100
print(inc1)






