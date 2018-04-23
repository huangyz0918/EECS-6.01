import lib601.dist as dist
import lib601.sm as sm
import lib601.ssm as ssm
import lib601.util as util

class StateEstimator(sm.SM):
	def __init__(self, model):
		self.model = model
		self.startState = model.startDistribution
	def getNextValues(self, state, inp):
		(o, i) = inp
		sGo = self.efficientBayesEvidence(state,o)
		dSPrime = self.transitionUpdate(sGo)
		return (dSPrime, dSPrime)
	def bayesEvidence(self,state,observation):	# form a JD then marginalize
		joint = dist.JDist(state, self.model.observationDistribution)
		belief = joint.conditionOnVar(1,observation)
		return belief
	def efficientBayesEvidence(self,state,observation):	# P(O|S)(observation distribution)*P(S)(state distribution)/P(O)
		bayesDict = {}
		normalizationCoefficient = 0.
		potentialStates = state.support()
		for outcome in potentialStates:	# P(O|S)*P(S)
			bayesDict[outcome] = self.model.observationDistribution(outcome).prob(observation)*state.prob(outcome)
			normalizationCoefficient += bayesDict[outcome]
 		for element in bayesDict.keys():	# normalize or /P(O)
 			bayesDict[element] = bayesDict[element]/normalizationCoefficient
		return dist.DDist(bayesDict)
	def transitionUpdate(self,belief):
		totalProbDict = {}
		normalizationCoefficient = 0.
		potentialStates = belief.support()
		for outcome in potentialStates: # P(St+1) = sum_t(P(St+1|I1,St)*P(St|O)	
			# iterates over St
			for possibility in potentialStates:	# iterates over St+1
				if possibility not in totalProbDict.keys():
					totalProbDict[possibility] = belief.prob(outcome)*self.model.transitionDistribution(0)(outcome).prob(possibility)
				else:
					totalProbDict[possibility] += belief.prob(outcome)*self.model.transitionDistribution(0)(outcome).prob(possibility)
		for outcome in totalProbDict.keys():	# calculate normalization coefficient
			normalizationCoefficient += totalProbDict[outcome]
		for outcome in totalProbDict.keys():	# normalize
			totalProbDict[outcome] = totalProbDict[outcome]/normalizationCoefficient
		return dist.DDist(totalProbDict)
	def totalProbability(self,belief):
		n = 0
		partialDist = {}
		for potentialState in belief.d.keys():		# go through states
			print "potentialState = ", potentialState
			partialDist[n] = self.model.transitionDistribution(0)(potentialState).d # what would it look like at this state
			for outcome in partialDist[n].keys():
				partialDist[n][outcome] *= belief.prob(potentialState)	# multiply by the probability of being in that state
			n+=1
		totalDist = partialDist[0]
		for event in partialDist[0].keys():
			for count in range(1,n):
				totalDist[event] += partialDist[count][event]		# normalize
		beliefPrime = dist.DDist(totalDist)
		print beliefPrime
		return beliefPrime

# Test

transitionTable = \
   {'good': dist.DDist({'good' : 0.7, 'bad' : 0.3}),
    'bad' : dist.DDist({'good' : 0.1, 'bad' : 0.9})}
observationTable = \
   {'good': dist.DDist({'perfect' : 0.8, 'smudged' : 0.1, 'black' : 0.1}),
    'bad': dist.DDist({'perfect' : 0.1, 'smudged' : 0.7, 'black' : 0.2})}

copyMachine = \
 ssm.StochasticSM(dist.DDist({'good' : 0.9, 'bad' : 0.1}),
                # Input is irrelevant; same dist no matter what
                lambda i: lambda s: transitionTable[s],
                lambda s: observationTable[s])
obs = [('perfect', 'step'), ('smudged', 'step'), ('perfect', 'step')]

cmse = StateEstimator(copyMachine)

print cmse.transduce(obs)

