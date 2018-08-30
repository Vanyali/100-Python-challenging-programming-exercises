'''
Please write a program to generate all sentences where subject is 
in ["I", "You"] and verb is in ["Play", "Love"] and 
the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.

'''

subjects = ["I", "You"]
verbs = ["Play", "Love"]
desports = ["Hockey","Football"]

for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(desports)):
            result = f"{subjects[i]} {verbs[j]} {desports[k]}"
            print(result)