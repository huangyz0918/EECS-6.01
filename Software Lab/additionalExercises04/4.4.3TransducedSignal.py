import lib601.sm as sm
import lib601.poly as poly
import lib601.sig
from lib601.sig import *
# Part 1: Implementation

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

def samplesInRange(sig,lo,hi):
	return [sig.sample(i) for i in range(lo,hi)]
	
class TransducedSignal(Signal):
	def __init__(self, s, m):
		self.s = s
		self.m = m
		self.pureMachine = self.m
	def sample(self, n):
		if n<0:
			return 0
		else:
			samples = samplesInRange(self.s,n,n+1)
			return self.m.transduce(samples)[-1]
			
# Part 2: Application
polyList = []
for i in range(51):
	if i == 0 or i == 20 or i == 50:
		polyList.append(100)
	else:
		polyList.append(0)
p = poly.Polynomial(polyList)
inputSig = polyR(UnitSampleSignal(),p)
bankLTISM = LTISM([1],[0.99],[],[0])
bankSig = TransducedSignal(inputSig,bankLTISM)
balance = samplesInRange(bankSig,0,61)

print "Value at time 10: ", balance[10]
print "Value at time 20: ", balance[20]
print "Value at time 30: ", balance[30]
print "Value at time 40: ", balance[40]
print "Value at time 50: ", balance[50]
print "Value at time 60: ", balance[60]




