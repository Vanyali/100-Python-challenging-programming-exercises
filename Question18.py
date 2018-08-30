'''
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import re
print("""******Rules******
\b\b At least 1 letter lower case!
\b\b At least 1 letter upper case!
\b\b At least 1 digit!
\b\b At least one of these symbols [$#@]
\b\b MAXIMUM LENGHT: 12
\b\b MINIMUM LENGHT: 6
""")

userpw = input("Write a password or passwords, i am gonna check it if they are decent!\n")
userpwlist = userpw.split(',')
userpwlistvalid = []
for pw in userpwlist:
    if len(pw) < 6:
        print("This password does not have minimum required to be safe...")
    elif len(pw) > 12:
        print("This password have to much character for decent password, you may forgot it soon... ")
    else:
        print("Minimum/Maximum lenght required is valid, let´s check the other 3 rules.\n")
        if re.search(r'[a-z]', pw) and re.search(r'[A-Z]', pw) and re.search(r'[.#$@]', pw):
            userpwlistvalid.append(pw)
            print("This password is valid! It was append to correct list!")
        else:
            print("There are no passwords valids.")

print(','.join(map(str,userpwlistvalid)))


        



