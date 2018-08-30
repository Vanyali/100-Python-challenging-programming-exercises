'''
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100

Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
import time

class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

user = Bank()

while True:
    userinput = input("Inser D-Deposit, W-Withdrawl or exit!")
    if userinput.lower() == "exit":
        print("Balance: ", user.get_balance())
        print("....Leaving....")
        time.sleep(2)
        break
    if userinput.lower() == 'd':
        dep = int(input("Amount of the deposit: "))
        user.deposit(dep)
    elif userinput.lower() == 'w':
        dep = int(input("Amount of the withdrawal: "))
        user.withdrawal(dep)
    else:
        pass


############################################################
'''
netAmount = 0 
while True:
    s = input()
    if s == "exit":
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netAmount += amount
    elif operation=="W":
        netAmount -= amount
    else:
        pass


print(netAmount)

'''
        




        
