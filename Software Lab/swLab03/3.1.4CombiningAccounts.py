import lib601.sm as sm

class BA1(sm.SM):
	startState = 0
	def getNextValues(self, state, inp):
		if inp != 0:
			newState = state * 1.02 + inp - 100
		else:
			newState = state * 1.02
		return (newState, newState)

class BA2(sm.SM):
	startState = 0
	def getNextValues(self, state, inp):
		newState = state * 1.01 + inp
		return (newState, newState)

class PureFunction(sm.SM):
	def __init__(self, f):
		self.f = f
	def getNextValues(self,state,inp):
		return (state,self.f(inp))
		
# Part 1: Maximize
# Make a state machine that computes the balances of both types of accounts
# and outputs the maximum of the two balances
# The input is a number
# Start by constructing a state machine whose input is a number and whose
# output is a tuple with two balances:
# Then combine this machine with sm.PureFunction


a1 = BA1()
a2 = BA2()
maxAccount = sm.Cascade(sm.Parallel(a1,a2),sm.PureFunction(max))

# maxAccount.transduce([1000,1500,2000,500],verbose = True)

# Part 2: Investment
# I put any deposit or withdrawal whose magnitude is > 3000 in the account1
# and all others in the account of type 2.  On every step both bank accounts
# should continue to earn relevant interest.  The output should be the sum
# of the balances in the two accounts.  Implement this by composing the two
# bank accoutns using sm.Parallel2 and cascading it with two simple machines
# you implement using sm.PureFunction

class Switcher(sm.SM):
	startState = None
	def getNextValues(self,state,inp):
		if abs(inp) > 3000:
			return (state, (inp,0))
		else:
			return (state, (0,inp))

def add(balances):
	return sum(balances)

switchAccount = sm.Cascade(Switcher(),sm.Cascade(sm.Parallel2(a1,a2),PureFunction(add)))

# switchAccount.transduce([1000,2000,4000,8000,-1000,-5000],verbose = True)