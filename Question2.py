'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

'''

def factorial_result(num):
    if num == 0:
        return 1  
    return num * factorial_result(num - 1)


valid_input = False
while not valid_input:
    try:
        num = int(input("Insert a number and you get the total factorial of that number!"))
    except ValueError:
        print("Not Letters please! Insert Integers!\n")
        continue
    if num < 0:
        print("Insert positive integers, please")
        continue
    else:
        break

func = factorial_result(num)
print(func)


    
