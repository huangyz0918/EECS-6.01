import lib601.sm as sm

# Part 1: Sum machine
# Define a terminating state machine class whose inputs are numbers, which
# outputs the sum of its inputs so far, and which terminates when the sum
# is > 100.  The current input should be reflected immediatley in the output
# at that time step.
class SumTSM(sm.SM):
	def __init__(self):
		self.startState = 0.
	def getNextValues(self,state,inp):
		return (state + inp, state + inp)
	def done(self,state):	# terminates when sum > 100
		return state > 100
		
		
a = SumTSM()
#a.transduce([2,4,8,16,32,64,128],verbose = True)
# 
# Part 2: Some machine
# Make a terminating state machine instance that repeats SumTSM four times
# then terminates.

fourTimes = sm.Repeat(a,4)

# Part 3: Counting Machine
# Define a terminating state machine class that counts from 1 up to a 
# specified number and then terminates.

class CountUpTo(sm.SM):
	def __init__(self,num):
		self.startState = 0
		self.endState = num
	def getNextValues(self,state,inp):
		return (state + 1, state + 1)
	def done(self,state):
		return state >= self.endState

m = CountUpTo(3)
# print m.run(n=20)	# runs the machine 20 times, or until termination

# Part 4: Multiple Counting Machine
def makeSequenceCounter(nums):
	smSequence = []
	for num in nums:
		smSequence.append(CountUpTo(num))
	return sm.Sequence(smSequence)
	
print makeSequenceCounter([2,5,3]).run(n=20)
