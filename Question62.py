'''
Please write assert statements to verify that every number in the list [2,4,6,8] is even.



Hints:
Use "assert expression" to make assertion.

'''

'''
Pyrhon assert statement is debugging aid that tests a condition. But if the assert condition evaluates to false, it raises an assertionError
exception with optional error message. The proper use of assertions is to inform developers about unrecoverable erros in program

'''

li = [2,4,6,8,10]
for i in li:
    assert i%2==0

for i in li:
    assert i%3==0


