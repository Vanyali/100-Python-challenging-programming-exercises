'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
from collections import Counter

string = "hello world! 123"

results = {"INTEGERS": 0, "LETTERS": 0}
for i in string:
    if i.isdigit():
        results["INTEGERS"] += 1
    elif i.isalpha():
        results["LETTERS"] += 1
    else:
        pass

print(results)
