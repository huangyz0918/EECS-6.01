import lib601.sm as sm
# Part 1: Simulate LTISM
# 
# m = LTISM([1,2],[1],[3],[4])
# Find the values returned by this machine for this input sequence:
# o = m.transduce([1,2,3,4,5])
# 
# x[-1] = 3, y[-1] = 4
# y[n] = x[n] + 2x[n-1] + y[n-1]
# 
# 1. o[0] = 11
# 2. o[1] = 15
# 3. o[2] = 22
# 4. o[3] = 32
# 5. o[4] = 45

# Part 2: Code

def dotProd(a,b):
	if len(a) == 0 or len(b) == 0: return 0
	if len(a) != len(b):
		print 'dotProd mismatch error ' + str(len(a)) + ' != ' +str(len(b))
	return sum([ai*bi for (ai,bi) in zip(a,b)])
	
class LTISM(sm.SM):
	def __init__(self, dCoeffs, cCoeffs, previousInputs = [], previousOutputs = []):
		self.cCoeffs = list(reversed(cCoeffs))
		self.dCoeffs = list(reversed(dCoeffs))
		self.j = len(self.dCoeffs)
		self.k = len(self.cCoeffs)
		self.previousInputs = previousInputs
		self.previousOutputs = previousOutputs
		# State is last j input values and last k input values
		self.startState = (previousInputs,previousOutputs)
	def getNextValues(self, state, input):
		(inputs, outputs) = state
		self.previousInputs.append(input)
		self.previousInputs = self.previousInputs[-self.j:]
		self.previousOutputs = self.previousOutputs[-self.k:]
		output = dotProd(self.previousInputs,self.dCoeffs)
		output += dotProd(self.previousOutputs,self.cCoeffs)
		self.previousOutputs.append(output)
		return ((self.previousInputs,self.previousOutputs),output)


a = LTISM([3],[])
a.transduce([1,2,3,4,5], verbose = True)

b = LTISM([0,1],[],[0],[])
b.transduce([1,2,3,4,5], verbose = True)


	
m = LTISM([1,2],[1],[3],[4])
m.transduce([1,2,3,4,5], verbose = True)
print m.transduce([1,2,3,4,5])