class Bank_Account():
 def __init__(self):
   self.balance=0
   self.accountnumber=int(input("Enter your Account number : "))
   self.name=input("Enter your name : ")
   self.accounttype=input("Enter your Account type : ")
 def display(self):
       print("Name : ",self.name)
       print("Account Number: ",self.accountnumber)
       print("Account type: ",self.accounttype)

 def deposit(self):
   amount=float(input("Enter amount to be Deposited: "))
   self.balance += amount
    print("\n Amount Deposited:",amount)

 def withdraw(self):
   amount = float(input("Enter amount to be Withdrawn: "))
 if self.balance>=amount:
   self.balance-=amount
      print("\n You Withdrew:", amount)
 else:
      print("\n Insufficient balance ")


s= Bank_Account()
s.deposit()
s.withdraw()
s.display()
