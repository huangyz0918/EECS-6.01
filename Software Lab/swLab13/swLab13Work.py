import lib601.search as search
import lib601.sm as sm


(farmer, goat, wolf, cabbage) = range(4)

class FarmerGoatWolfCabbage(sm.SM):
	startState = ('L','L','L','L')
	legalInputs = ['takeGoat','takeNone','takeWolf','takeCabbage']
	def __init__(self):
		self.goal = ('R','R','R','R')
	def nextState(self,state,action):
		nextState = list(state)
		if action == 'takeGoat':
			nextState = self.farmerTakesItem(nextState,1)
		elif action == 'takeNone':
			if state[0] == 'R':
				nextState[0] = 'L'
			else:
				nextState[0] = 'R'
		elif action == 'takeWolf':
			nextState = self.farmerTakesItem(nextState,2)
		elif action == 'takeCabbage':
			nextState = self.farmerTakesItem(nextState,3)
		if self.doesAnyoneDie(nextState):	
			return state
		return tuple(nextState)
	def farmerTakesItem(self,nextState,itemIndex):
		if nextState [0] == nextState[itemIndex]:
			if nextState[0] == 'R':
				nextState[0] = 'L'
				nextState[itemIndex] = 'L'
			elif nextState[0] == 'L':
				nextState[0] = 'R'
				nextState[itemIndex] = 'R'
		return nextState
	def doesAnyoneDie(self,nextState):
		if nextState[1] == nextState[3] and nextState[0] != nextState[1]:
			return True
		elif nextState[1] == nextState[2] and nextState[0] != nextState[1]:
			return True
		else:
			return False
	def getNextValues(self, state, action):
		nextState = self.nextState(state,action)
		return (nextState, nextState)
	def done(self, state):
		return state == self.goal
      
sm = FarmerGoatWolfCabbage()
sm.transduce(['takeGoat','takeNone','takeNone'],verbose = True)
  
