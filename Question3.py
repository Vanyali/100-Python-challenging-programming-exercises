'''
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''
def valid_input():
    while True:
        try:
            num = int(input("Insert a number and you get the total factorial of that number!"))
            return num
        except ValueError:
            print("Not Letters please! Insert Integers!\n")
            continue
        if num < 0:
            print("Insert positive integers, please")
            continue
        else:
            break

num1 = valid_input()

def dict_i_square(num):
    d = dict()
    for i in range(1,num +1):
        d[i] = i * i
    return d

print(dict_i_square(num1))



        
        




