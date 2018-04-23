import lib601.sm as sm

class Cascade(sm.SM):
	def __init__(self,sm1,sm2):
		self.m1 = sm1
		self.m2 = sm2
		self.startState = (sm1.startState, sm2.startState)
	def getNextValues(self,state,inp):
		(s1,s2) = state if state else (self.m1.startState, self.m2.startState)
		(newS1,o1) = self.m1.getNextValues(s1,inp)
		(newS2,o2) = self.m2.getNextValues(s2,o1)
		return ((newS1,newS2),o2)

class Delay(sm.SM):
	def __init__(self,v0):
		self.startState = v0
	def getNextValues(self,state,inp):
		# output is old state
		return (inp,state)

sm1 = Delay(1)
sm2 = Delay(2)
c = Cascade(sm1,sm2)
c.transduce([3,5,7,9],verbose = True)