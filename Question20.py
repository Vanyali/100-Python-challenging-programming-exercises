'''
Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

'''

class iterator:
    def __init__(self, n):
        self.n = n

    def divBySeven(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i 





'''
print(iterator(100).divBySeven())
print(next(iterator(100).divBySeven()))
print(next(iterator(100).divBySeven()))
'''

'''
for num in iterator(100).divBySeven():
    print(num)
    '''

