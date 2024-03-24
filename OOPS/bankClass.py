import sys
class Bank:
    """Bank related transactions"""
    def __init__(self,name='',balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if self.balance<amount:
            print("Not enough balance")
        else:
            self.balance -= amount
        return self.balance
name=input("Enter name: ")
b=Bank(name)
while True:
    print("d-Deposit, w-Withdraw, e-Exit")
    choice=input("Your choice: ")
    if choice=='e' or choice=='E':
        sys.exit()
    amt=float(input("Enter amount: "))
    if choice=='d' or choice=='D':
        print("Balance after deposit is ",b.deposit(amt))
    elif choice=='w' or choice=='W':
        print("Balance after withdrawal is ", b.withdraw(amt))


