class AccountDollars():
	def __init__(self,initialBalance):
		self.Balance = initialBalance
		self.interestRate = 0.03
		self.fee = 20
	def depositDollars(self,depositAmount):
		self.Balance = self.Balance*(1.+self.interestRate) - self.fee + depositAmount
		return self.Balance
		
x = AccountDollars(200)
print x.depositDollars(300)

class AccountPounds(AccountDollars):
	def __init__(self,initialBalance):
		AccountDollars.__init__(self, 2.*initialBalance)	# here I convert pounds to dollars
	def depositPounds(self,depositAmount):
		return self.depositDollars(2.*depositAmount)/2.	# converting back to pounds

x = AccountPounds(100)
print x.depositPounds(150)
print x.depositDollars(300)