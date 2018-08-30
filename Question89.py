'''
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.

'''

def chinese_puzzle(numheads,numlegs):
    ns=0
    for i in range(numheads+1):
        j=numheads-i

        if 2*i+4*j==numlegs:
            return i,j
            
    return ns,ns


solutions=chinese_puzzle(35,94)
print(solutions)



    
