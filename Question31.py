'''
Define a function that can accept an integer number as input and print the "It is an even number" 
if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.

'''

def odd_or_even(num):
    if num % 2 == 0:
        print(num, "It's a even number!")
    else:
        print(num, "It's odd number!")

odd_or_even(4)

odd_or_even(5)