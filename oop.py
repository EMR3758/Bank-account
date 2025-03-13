from bank_account import * 

Emir = BankAccount(500,"Emir")
Esma = BankAccount(1000,"Esma")

#Public değişkenlere erişim,protected değişkene erişim(dışarıdan erişilebilir ama önerilmez.)
#Private değişkenlere dışarıdan erişilemez.


#Bakiye sorgulama
Emir.getbalance()
Esma.getbalance()

#Para yatırma
Emir.deposit(500)

#Para çekme
Esma.withdraw(1000)
Esma.withdraw(10)

Emir.transfer(300,Esma)

Zafer = InterestRewardsAcct(1000,"Zafer")

Zafer.getbalance()
Zafer.deposit(100)
Zafer.transfer(100,Emir)

Ayşe = SavingAcct(1000,"Ayşe")
Ayşe.getbalance()
Ayşe.deposit(100)
Ayşe.transfer(1000,Esma)