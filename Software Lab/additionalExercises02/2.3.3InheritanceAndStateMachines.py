import lib601.sm as sm
# Define the CountingStateMachine class.  Provide defs for startState
# and getNextValues.  getNextValues should use getOutput to produce the
# output for a given state and inp.

# States are always integers that start at 0 and increment by 1 on each
# transition

class CountingStateMachine(sm.SM):
	def __init__(self):
		self.startState = 0
	def getNextValues(self, state, inp):
		return (self.getOutput(state+1,inp),self.getOutput(state,inp))

class CountMod5(CountingStateMachine):
	def getOutput(self,state,inp):
# 		print "state%5 = ", state%5
		return state%5

# Then define a subclass of CountingStateMachine called Alternate Zeros.  Instances
# of AlternateZeros should be state machines for which, on even steps, the output
# is the same as the input, and on odd steps, the output is 0.


# It can't know the next state if the count is going to be even, since its the inp
class AlternateZeros(CountingStateMachine):
	def getNextValues(self,state,inp):
		return (state + 1, self.getOutput(state,inp))	# the state is a simple count
	def getOutput(self,state,inp):
		if state%2 == 0:
			return inp
		else:
			return 0
		
list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = [0,2,0,4,0,6,0,8,0,10]
a = CountMod5()
a.transduce([3,1,2,5,9], verbose = True)
a.transduce(list1,verbose = True)
a.transduce(list2,verbose = True)

b = AlternateZeros()
b.transduce([3,1,2,5,9], verbose = True)
b.transduce(list1,verbose = True)
b.transduce(list2,verbose = True)
