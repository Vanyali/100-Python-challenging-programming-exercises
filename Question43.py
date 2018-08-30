'''
Question:
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.

'''

user = input("Yes or No")
if  user.lower() in ["Yes", "Y", "YES", "yes", "YeS", ""]:
    print("Yes")
else:
    print("No")

