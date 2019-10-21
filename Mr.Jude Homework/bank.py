#%%
class Account:
    _balance = 0
    
    def __init__(self, balance2):
        self._balance = balance2
    
    def getbalance(self):
        return self._balance
   
    def deposit(self,amt):
        if amt > 0:
            self._balance = self._balance + amt
            return True
        else:
            return False
        
    def withdraw(self,amt):
        try:
            if amt <= 0:
                return False
            else:
                self._balance = amt
                return True
        except TypeError:
            return False
        
myAccount = Account(5000)

if (myAccount.deposit(10000)):
    print("Account balance is >>",myAccount.getbalance())
        
class Customer:
    _firstname = ""
    _lastname = ""
    _account = Account(5000)
    
    def __init__(self,firstname,lastname):
        self._firstname = firstname
        self._lastname = lastname
    
    def getfname(self):
        return self._firstname
    
    def getlname(self):
        return self._lastname
    
    def getaccount(self):
        return self._account
    
    def setaccount(self, acct):
        self._account = acct

class Bank:
    _customers = []
    _number_of_customers = 0
    _bankname = ""
    
    def __init__(self,customers,numberofcustomers,bankname):
        self._customers = customers
        self._number_of_customers = numberofcustomers
        self._bankname = bankname
    
    def addcustomer(self,firstname,lastname):
        if (firstname,lastname) not in self._customers:
            self._customers.append(firstname + lastname)
            self._number_of_customers += 1
    
    def getcustomer(self):
        return self._customers
            
    
myAccount = Account(5000)

if (myAccount.deposit(10000)):
    print("Account balance is >>",myAccount.getbalance())

myfcustomer = "Mia Ozawa"



myBank = "Big OOO"
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

    
