'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
'''
input_s = input("Insert row and column with comma.")
lst = []
for i in input_s.split(','):
    lst.append(int(i))
rowdim = lst[0]
columndim = lst[1]

multilist = []
for row in range(rowdim):
    newtable = []
    for column in range(columndim):
        newtable.append(0)
    multilist.append(newtable)

#multilist = [[0 for col in range(columndim)]for row in range(rowdim)]
print(multilist)
print()


for row in range(rowdim):
    for column in range(columndim):
        multilist[row][column] = row * column

print(multilist)    



