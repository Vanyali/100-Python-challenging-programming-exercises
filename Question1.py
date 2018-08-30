'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

'''


lst = []
for i in range(2000, 3001):
    if i%7==0 and i%5 !=0:
        lst.append(str(i))

print(lst)
total_numbers = len(lst)
print(f"{total_numbers} numbers in lst!")
print(','.join(lst))




    