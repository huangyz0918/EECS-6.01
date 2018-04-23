import lib601.sm as sm

# Define negate to be an instance of sm.PureFunction that takes a boolean
# and returns the negation of it
def negFunct(boolean):
	return not boolean

class PureFunction(sm.SM):
	def __init__(self, f):
		self.f = f
	def getNextValues(self,state,inp):
		return (state,self.f(inp))

negate = sm.PureFunction(negFunct)
# negate.transduce([True,False],verbose = True)

# Use sm.Feedback,sm.Cascade, and negate to construct an instance whose output alternates
# between True and False for any input sequence; starting with true.

alternating = sm.Feedback(sm.Cascade(sm.Delay(False),negate))
alternating.transduce([1,True,False,True,False,True,False],verbose = True)

# Not totally sure how I made this work, but hey it does.