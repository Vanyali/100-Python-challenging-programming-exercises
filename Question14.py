'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

string = "Hellow world!"

results = {"UPPER": 0, "LOWER": 0 }
for i in string:
    if i.islower():
        results["LOWER"] += 1
    elif i.isupper():
        results["UPPER"] += 1
    else:
        pass

print(results)
print()
print("Upper Case Letters: ",results["UPPER"])
print()
print("Lower Case Letters: ", results["LOWER"])

