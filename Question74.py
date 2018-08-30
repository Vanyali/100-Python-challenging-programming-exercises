'''
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints:
Use timeit() function to measure the running time.

'''

import time
from timeit import Timer


first = time.time()
for _ in range(100):
    a = 1 + 1
    print(a)
last = time.time()

print()
print("Finish: ", last - first)




