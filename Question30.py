'''
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.

Hints:
Use len() function to get the length of a string

'''

def bigger_string(string1, string2):

    strg1 = len(string1)
    strg2 = len(string2)
    if strg1 > strg2:
        return string1
    elif strg1 < strg2:
        return string2
    else:
        return string1 + "\n" + string2
        

print(bigger_string("Hello I am Noddy", "Hello"))
print()
print(bigger_string("Hello I am Noddy", "Hello I Like Python and You?"))
print()
print(bigger_string("Hello I am Noddy", "Hello I am Noddi"))



    