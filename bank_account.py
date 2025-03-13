class BalanceException(Exception):
    pass

#__private :Çift alt çizgi(__) ile belirtilir.Bu değişkenlere doğrudan dışarıdan erişilemez,sadece sınıf içinden erişilebilir.

class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount name : '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def getbalance(self):
        print(f"\nAccount name : '{self.name}'\nBalance = ${self.balance:.2f}")
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.\nAccount name : '{self.name}'\nBalance = ${self.balance:.2f}")
    
    def viableTransaction(self , amount):
        if self.balance >= amount:
            return
        else: 
            raise BalanceException(
                f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
    
    def transfer(self,amount,account):
        try:
            print("\n**********\n\nBeginning Tranfer..")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!\n\n*********")
        except BalanceException as error:
            print(f"\nTransfer interrupted: {error}")
    
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getbalance()

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount+self.fee)
            print("\nWithdraw complete.")
            self.getbalance()
        except BalanceException as error:
            print("\nWithdraw interrupted : {error}")        