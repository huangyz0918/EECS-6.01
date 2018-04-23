import lib601.sm as sm

class Delay(sm.SM):
	def __init__(self,v0):
		self.startState = v0
	def getNextValues(self,state,inp):
		# output is old state
		return (inp,state)

class Increment(sm.SM):
	startState = 0
	def __init__(self,incr):
		self.incr = incr
	def getNextValues(self,state,inp):
		return (state, inp + self.incr)
		
# Fill in the behavior tables
# Note: list indexes correspond to times, e.g. list[1] -> list at t=1
# 1.
sm1 = Delay(1)
sm2 = Delay(2)
c = sm.Cascade(sm1,sm2)
c.transduce([3,5,7,9])

# cascade means we take the output of the first sm as the input
# for the second
sm1input = [3,5,7,9]
sm1state = [1,3,5,7,9]
sm1output = [1,3,5,7]
sm2input = [1,3,5,7]
sm2state = [2,1,3,5,7]
sm2output = [2,1,3,5]

# 2.
sm1 = Delay(1)
sm2 = Increment(3)
c = sm.Cascade(sm1,sm2)
c.transduce([3,5,7,9]) #,verbose = True)

sm1input = [3,5,7,9]
sm1state = [1,3,5,7,9]
sm1output = [1,3,5,7]
sm2input = [1,3,5,7]
sm2state = [0,0,0,0,0]
sm2output = [4,6,8,10]