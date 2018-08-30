'''
Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints:
Use eval() to evaluate an expression.

'''



expression = input("Insert expression mathematical, with input keyword it's going to be a string but using eval going to do the match anyways!")
print(eval(expression))

#for example, without input
print(eval("3+5"))
