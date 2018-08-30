'''
Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints: Use int() to convert a string to integer.

'''

def two_int_string_sum(num1,num2):
    result = int(num1) + int(num2)
    return result

print(two_int_string_sum("3","3"))

