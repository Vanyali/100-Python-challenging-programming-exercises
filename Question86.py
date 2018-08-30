'''
Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

Hints:
Use list[::-1] to iterate a list in a reverse order.


'''

string = "rise to vote sir"
string_rever = reversed(string)
new_lst = []
for i in string_rever:
    new_lst.append(i)
print("".join(new_lst))


#Or

string = "rise to vote sir"
print(string[::-1])



