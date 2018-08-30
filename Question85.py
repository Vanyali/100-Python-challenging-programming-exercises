'''
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.

'''

string ='abcdefgabc'
new_dic = {}
for i in string:
    new_dic[i] = new_dic.get(i, 0) + 1
print(new_dic)

